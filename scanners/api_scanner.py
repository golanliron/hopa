"""API scanner for structured grant APIs (e.g., Grants.gov)."""

import json
import logging

import requests

from scanners.base import BaseScanner, CallForProposal
from config import INTERNATIONAL_SOURCES, REQUEST_HEADERS, REQUEST_TIMEOUT

logger = logging.getLogger(__name__)


class APIScanner(BaseScanner):
    """Scans structured APIs for calls for proposals."""

    def scan(self) -> list[CallForProposal]:
        results = []
        api_sources = [s for s in INTERNATIONAL_SOURCES if s["type"] == "api"]

        for source in api_sources:
            logger.info("Scanning API: %s", source["name"])
            try:
                calls = self._scan_api(source)
                results.extend(calls)
                logger.info("Found %d calls from %s", len(calls), source["name"])
            except Exception as e:
                logger.error("Error scanning API %s: %s", source["name"], e)

        return results

    def _scan_api(self, source: dict) -> list[CallForProposal]:
        """Scan a REST API source."""
        url = source["url"]
        params = source.get("api_params", {})

        try:
            response = requests.post(
                url,
                headers={**REQUEST_HEADERS, "Content-Type": "application/json"},
                json=params,
                timeout=REQUEST_TIMEOUT,
            )
            response.raise_for_status()
            data = response.json()
        except (requests.RequestException, json.JSONDecodeError) as e:
            logger.error("API request failed for %s: %s", source["name"], e)
            return []

        calls = []

        # Handle Grants.gov response format
        opportunities = data.get("oppHits", data.get("opportunities", []))
        if isinstance(opportunities, list):
            for opp in opportunities[:50]:  # Limit to 50 most recent
                title = opp.get("title", opp.get("oppTitle", ""))
                opp_id = opp.get("id", opp.get("oppNumber", ""))
                close_date = opp.get("closeDate", opp.get("archiveDate", ""))
                agency = opp.get("agency", opp.get("agencyName", ""))
                description = opp.get("description", opp.get("synopsis", ""))

                if not title:
                    continue

                link = f"https://www.grants.gov/search-results-detail/{opp_id}" if opp_id else url

                calls.append(
                    CallForProposal(
                        title=title,
                        source=f"{source['name']} ({agency})" if agency else source["name"],
                        url=link,
                        category=source["category"],
                        region="international",
                        description=str(description)[:300] if description else "",
                        deadline=close_date,
                    )
                )

        return calls
