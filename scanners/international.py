"""Scanner for international calls for proposals."""

import logging
from urllib.parse import urljoin

from scanners.base import BaseScanner, CallForProposal
from config import INTERNATIONAL_SOURCES

logger = logging.getLogger(__name__)

MAX_DEEP_SCANS_PER_SOURCE = 10


class InternationalScanner(BaseScanner):
    """Scans international sources for calls for proposals."""

    def scan(self) -> list[CallForProposal]:
        results = []
        for source in INTERNATIONAL_SOURCES:
            if source["type"] in ("rss", "api"):
                continue  # Handled by RSSScanner / APIScanner
            logger.info("Scanning: %s (%s)", source["name"], source["url"])
            try:
                calls = self._scan_source(source)
                results.extend(calls)
                logger.info("Found %d calls from %s", len(calls), source["name"])
            except Exception as e:
                logger.error("Error scanning %s: %s", source["name"], e)
        return results

    def _scan_source(self, source: dict) -> list[CallForProposal]:
        soup = self.fetch_page(source["url"])
        if not soup:
            return []

        raw_calls = self._extract_calls(soup, source)

        # Convert to CallForProposal and deep-scan
        calls = []
        for i, raw in enumerate(raw_calls):
            call = CallForProposal(
                title=raw.get("title", ""),
                source=source["name"],
                url=raw.get("url", source["url"]),
                category=source["category"],
                region="international",
                description=raw.get("description", ""),
                deadline=raw.get("deadline"),
                grant_amount=raw.get("grant_amount"),
            )

            # Deep scan for missing details
            if i < MAX_DEEP_SCANS_PER_SOURCE and (
                not call.description or not call.deadline
            ):
                if call.url != source["url"]:
                    logger.debug("Deep scanning: %s", call.url)
                    details = self.deep_scan_page(call.url)
                    if details.get("description") and not call.description:
                        call.description = details["description"]
                    if details.get("deadline") and not call.deadline:
                        call.deadline = details["deadline"]
                    if details.get("grant_amount") and not call.grant_amount:
                        call.grant_amount = details["grant_amount"]

            calls.append(call)

        # Deduplicate
        seen = set()
        unique = []
        for c in calls:
            if c.url not in seen:
                seen.add(c.url)
                unique.append(c)
        return unique

    def _extract_calls(self, soup, source: dict) -> list[dict]:
        """Extract call items from a listing page."""
        calls = []

        # Try common article patterns
        articles = soup.select(
            "article, .post, .entry, .call-item, .grant-item, "
            ".opportunity, .views-row, .card, .list-item, "
            ".funding-item, .opportunity-card"
        )
        if articles:
            for article in articles:
                call = self._extract_from_article(article, source)
                if call:
                    calls.append(call)

        # Fallback: scan for relevant links
        if not calls:
            links = soup.select("a[href]")
            for link in links:
                title = link.get_text(strip=True)
                href = link.get("href", "")
                if self._is_grant_link(title, href):
                    full_url = urljoin(source["url"], href)
                    calls.append({
                        "title": title,
                        "url": full_url,
                    })

        return calls

    def _extract_from_article(self, article, source: dict) -> dict | None:
        """Extract call info from an article element."""
        title_el = article.select_one("h1, h2, h3, h4, .title, .entry-title, .card-title")
        link_el = article.select_one("a[href]")

        if title_el:
            title = title_el.get_text(strip=True)
        elif link_el:
            title = link_el.get_text(strip=True)
        else:
            return None

        if not title or len(title) < 5:
            return None

        url = urljoin(source["url"], link_el.get("href", "")) if link_el else source["url"]

        desc_el = article.select_one(".excerpt, .summary, .description, p, .entry-content")
        description = desc_el.get_text(strip=True)[:300] if desc_el else ""

        # Extract deadline
        import re
        deadline = None
        for text in article.stripped_strings:
            text_lower = text.lower()
            if any(kw in text_lower for kw in ["deadline", "due date", "closing", "expires"]):
                match = re.search(r"(\d{1,2}[/.]\d{1,2}[/.]\d{2,4}|\w+ \d{1,2},? \d{4})", text)
                if match:
                    deadline = match.group(0)
                else:
                    deadline = text[:100]
                break

        # Extract grant amount
        grant_amount = None
        for text in article.stripped_strings:
            if any(c in text for c in ["$", "€", "£"]):
                match = re.search(r"[\$€£][\d,.]+[KMBkmb]?", text)
                if match:
                    grant_amount = match.group(0)
                    break

        return {
            "title": title,
            "url": url,
            "description": description,
            "deadline": deadline,
            "grant_amount": grant_amount,
        }

    def _is_grant_link(self, title: str, href: str) -> bool:
        """Check if a link is likely a grant/call opportunity."""
        if not title or len(title) < 10:
            return False
        skip = ["menu", "nav", "footer", "login", "sign up", "cookie", "privacy"]
        title_lower = title.lower()
        if any(s in title_lower for s in skip):
            return False
        relevant = [
            "grant", "call", "proposal", "fund", "opportunity",
            "fellowship", "residency", "award", "open call",
            "submit", "application", "deadline",
        ]
        return any(r in title_lower for r in relevant)
