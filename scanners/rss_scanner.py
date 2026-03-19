"""RSS feed scanner for calls for proposals."""

import logging

try:
    import feedparser
except ImportError:
    feedparser = None

from scanners.base import BaseScanner, CallForProposal
from config import INTERNATIONAL_SOURCES

logger = logging.getLogger(__name__)


class RSSScanner(BaseScanner):
    """Scans RSS feeds for calls for proposals."""

    def scan(self) -> list[CallForProposal]:
        if feedparser is None:
            logger.warning("feedparser not installed - skipping RSS sources. Install with: pip install feedparser")
            return []

        results = []
        rss_sources = [s for s in INTERNATIONAL_SOURCES if s["type"] == "rss"]

        for source in rss_sources:
            logger.info("Scanning RSS: %s", source["name"])
            try:
                calls = self._scan_feed(source)
                results.extend(calls)
                logger.info("Found %d calls from %s", len(calls), source["name"])
            except Exception as e:
                logger.error("Error scanning RSS %s: %s", source["name"], e)

        return results

    def _scan_feed(self, source: dict) -> list[CallForProposal]:
        content = self.fetch_raw(source["url"])
        if not content:
            return []

        feed = feedparser.parse(content)
        calls = []

        for entry in feed.entries:
            title = getattr(entry, "title", "")
            link = getattr(entry, "link", "")
            summary = getattr(entry, "summary", "")
            published = getattr(entry, "published", None)

            if not title:
                continue

            # Clean up summary
            if summary:
                from bs4 import BeautifulSoup
                summary = BeautifulSoup(summary, "lxml").get_text(strip=True)[:300]

            calls.append(
                CallForProposal(
                    title=title,
                    source=source["name"],
                    url=link,
                    category=source["category"],
                    region="international",
                    description=summary,
                    deadline=published,
                )
            )

        return calls
