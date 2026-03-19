"""Scanner for international calls for proposals."""

import logging
from urllib.parse import urljoin

from scanners.base import BaseScanner, CallForProposal
from config import INTERNATIONAL_SOURCES

logger = logging.getLogger(__name__)


class InternationalScanner(BaseScanner):
    """Scans international sources for calls for proposals."""

    def scan(self) -> list[CallForProposal]:
        results = []
        for source in INTERNATIONAL_SOURCES:
            if source["type"] == "rss":
                continue  # Handled by RSSScanner
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
                    calls.append(
                        CallForProposal(
                            title=title,
                            source=source["name"],
                            url=full_url,
                            category=source["category"],
                            region="international",
                        )
                    )

        # Deduplicate
        seen = set()
        unique = []
        for c in calls:
            if c.url not in seen:
                seen.add(c.url)
                unique.append(c)
        return unique

    def _extract_from_article(
        self, article, source: dict
    ) -> CallForProposal | None:
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
        deadline = None
        for text in article.stripped_strings:
            text_lower = text.lower()
            if any(kw in text_lower for kw in ["deadline", "due date", "closing", "expires"]):
                deadline = text[:100]
                break

        # Extract grant amount
        grant_amount = None
        for text in article.stripped_strings:
            text_lower = text.lower()
            if any(c in text_lower for c in ["$", "€", "£", "usd", "eur"]):
                grant_amount = text[:100]
                break

        return CallForProposal(
            title=title,
            source=source["name"],
            url=url,
            category=source["category"],
            region="international",
            description=description,
            deadline=deadline,
            grant_amount=grant_amount,
        )

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
