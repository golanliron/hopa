"""Scanner for Israeli calls for proposals (קולות קוראים מישראל)."""

import logging
import re
from urllib.parse import urljoin

from scanners.base import BaseScanner, CallForProposal
from scanners.extractors import get_extractor, get_api_extractor
from config import ISRAELI_SOURCES

logger = logging.getLogger(__name__)

# Max number of detail pages to deep-scan per source (to avoid overloading)
MAX_DEEP_SCANS_PER_SOURCE = 10

# Keywords that indicate a real call for proposals (at least one must match)
RELEVANCE_KEYWORDS_HE = [
    "קול קורא", "מענק", "תמיכה", "הגשה", "מלגה", "מימון", "תקציב",
    "קרן", "מכרז", "הזמנה", "תוכנית", "פרויקט", "סיוע", "השקעה",
    "מסלול", "שובר", "אקסלרטור", "חממה", "שיתוף פעולה",
]
RELEVANCE_KEYWORDS_EN = [
    "grant", "call", "proposal", "fund", "submit", "application",
    "fellowship", "award", "program", "initiative", "deadline",
]


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
        # Try API-based extractor first (structured data, most reliable)
        api_extractor = get_api_extractor(source["url"])
        if api_extractor:
            raw_calls = api_extractor()
            if raw_calls:
                logger.debug(
                    "API extractor found %d calls for %s",
                    len(raw_calls),
                    source["name"],
                )
                # API results are already detailed, skip deep scanning
                calls = []
                for raw in raw_calls:
                    call = CallForProposal(
                        title=raw.get("title", ""),
                        source=source["name"],
                        url=raw.get("url", source["url"]),
                        category=source["category"],
                        region="israel",
                        description=raw.get("description", ""),
                        deadline=raw.get("deadline"),
                        grant_amount=raw.get("grant_amount"),
                    )
                    calls.append(call)
                # Deduplicate
                seen = set()
                return [c for c in calls if c.url not in seen and not seen.add(c.url)]

        # Fall back to HTML scraping
        soup = self.fetch_page(source["url"])
        if not soup:
            return []

        extractor = get_extractor(source["url"])
        if extractor:
            raw_calls = extractor(soup, source)
            logger.debug(
                "Source-specific extractor found %d calls for %s",
                len(raw_calls),
                source["name"],
            )
        else:
            raw_calls = self._generic_extract(soup, source)

        # Convert to CallForProposal objects and deep-scan for details
        calls = []
        for i, raw in enumerate(raw_calls):
            call = CallForProposal(
                title=raw.get("title", ""),
                source=source["name"],
                url=raw.get("url", source["url"]),
                category=source["category"],
                region="israel",
                description=raw.get("description", ""),
                deadline=raw.get("deadline"),
                grant_amount=raw.get("grant_amount"),
            )

            # Deep scan individual pages for missing details
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
                    if details.get("page_title") and len(call.title) < 10:
                        call.title = details["page_title"]

            calls.append(call)

        # Deduplicate by URL and filter irrelevant results
        seen_urls = set()
        unique_calls = []
        for call in calls:
            if call.url not in seen_urls and self._is_relevant_call(call):
                seen_urls.add(call.url)
                unique_calls.append(call)

        return unique_calls

    def _is_relevant_call(self, call: CallForProposal) -> bool:
        """Check if a call is actually relevant (not a blog post, nav link, etc.)."""
        text = f"{call.title} {call.description}".lower()
        all_keywords = RELEVANCE_KEYWORDS_HE + RELEVANCE_KEYWORDS_EN
        # At least one keyword should match in title or description
        if any(kw in text for kw in all_keywords):
            return True
        # If it has a deadline, it's likely a real call
        if call.deadline:
            return True
        # If title is long enough and from a known source, keep it
        if len(call.title) >= 20:
            return True
        return False

    def _generic_extract(self, soup, source: dict) -> list[dict]:
        """Generic extraction for sources without a specific extractor."""
        calls = []

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

        # Pattern 2: Try links with relevant keywords
        if not calls:
            links = soup.select("a[href]")
            for link in links:
                title = link.get_text(strip=True)
                href = link.get("href", "")
                if self._is_relevant_link(title, href):
                    full_url = urljoin(source["url"], href)
                    calls.append({
                        "title": title,
                        "url": full_url,
                    })

        return calls

    def _extract_from_article(self, article, source: dict) -> dict | None:
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
                import re
                match = re.search(r"(\d{1,2}[/.]\d{1,2}[/.]\d{2,4})", text)
                if match:
                    deadline = match.group(1)
                else:
                    deadline = text[:100]
                break

        return {
            "title": title,
            "url": url,
            "description": description,
            "deadline": deadline,
        }

    def _is_relevant_link(self, title: str, href: str) -> bool:
        """Check if a link is relevant to calls for proposals."""
        if not title or len(title) < 10:
            return False
        skip_words = [
            "menu", "nav", "footer", "header", "contact", "about",
            "צור קשר", "אודות", "תפריט",
        ]
        title_lower = title.lower()
        if any(w in title_lower for w in skip_words):
            return False
        relevant_words = [
            "קול קורא", "מענק", "תמיכה", "הגשה", "מלגה",
            "grant", "call", "proposal", "fund", "submit",
        ]
        return any(w in title_lower for w in relevant_words)
