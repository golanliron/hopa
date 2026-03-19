"""Scanner for Israeli calls for proposals (קולות קוראים מישראל)."""

import logging
from urllib.parse import urljoin

from scanners.base import BaseScanner, CallForProposal
from config import ISRAELI_SOURCES

logger = logging.getLogger(__name__)


class IsraeliScanner(BaseScanner):
    """Scans Israeli sources for calls for proposals."""

    def scan(self) -> list[CallForProposal]:
        results = []
        for source in ISRAELI_SOURCES:
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

        # Try multiple common patterns for extracting links and titles
        # Pattern 1: Article/post entries
        articles = soup.select(
            "article, .post, .entry, .call-item, .grant-item, "
            ".views-row, .node, .item-list li"
        )
        if articles:
            for article in articles:
                call = self._extract_from_article(article, source)
                if call:
                    calls.append(call)

        # Pattern 2: If no articles found, try links with common patterns
        if not calls:
            links = soup.select("a[href]")
            for link in links:
                title = link.get_text(strip=True)
                href = link.get("href", "")
                if self._is_relevant_link(title, href):
                    full_url = urljoin(source["url"], href)
                    calls.append(
                        CallForProposal(
                            title=title,
                            source=source["name"],
                            url=full_url,
                            category=source["category"],
                            region="israel",
                        )
                    )

        # Deduplicate by URL
        seen_urls = set()
        unique_calls = []
        for call in calls:
            if call.url not in seen_urls:
                seen_urls.add(call.url)
                unique_calls.append(call)

        return unique_calls

    def _extract_from_article(
        self, article, source: dict
    ) -> CallForProposal | None:
        """Extract call info from an article element."""
        # Find the title - try heading first, then first link
        title_el = article.select_one("h1, h2, h3, h4, .title, .entry-title")
        link_el = article.select_one("a[href]")

        if title_el:
            title = title_el.get_text(strip=True)
        elif link_el:
            title = link_el.get_text(strip=True)
        else:
            return None

        if not title or len(title) < 5:
            return None

        # Get URL
        if link_el:
            url = urljoin(source["url"], link_el.get("href", ""))
        else:
            url = source["url"]

        # Get description
        desc_el = article.select_one(
            ".excerpt, .summary, .description, p, .entry-content"
        )
        description = desc_el.get_text(strip=True)[:300] if desc_el else ""

        # Try to find deadline
        deadline = None
        for text in article.stripped_strings:
            text_lower = text.lower()
            if any(
                kw in text_lower
                for kw in ["מועד", "דדליין", "deadline", "תאריך אחרון", "עד ליום"]
            ):
                deadline = text[:100]
                break

        return CallForProposal(
            title=title,
            source=source["name"],
            url=url,
            category=source["category"],
            region="israel",
            description=description,
            deadline=deadline,
        )

    def _is_relevant_link(self, title: str, href: str) -> bool:
        """Check if a link is relevant to calls for proposals."""
        if not title or len(title) < 10:
            return False
        # Skip navigation/menu links
        skip_words = [
            "menu", "nav", "footer", "header", "contact", "about",
            "צור קשר", "אודות", "תפריט",
        ]
        title_lower = title.lower()
        if any(w in title_lower for w in skip_words):
            return False
        # Look for relevant keywords
        relevant_words = [
            "קול קורא", "מענק", "תמיכה", "הגשה", "מלגה",
            "grant", "call", "proposal", "fund", "submit",
        ]
        return any(w in title_lower for w in relevant_words)
