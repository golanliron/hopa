"""Base scanner class and data models."""

import logging
import re
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Optional

import requests
from bs4 import BeautifulSoup

from config import REQUEST_HEADERS, REQUEST_TIMEOUT, MAX_RETRIES, RETRY_DELAY

logger = logging.getLogger(__name__)


@dataclass
class CallForProposal:
    """Represents a single call for proposal / קול קורא."""

    title: str
    source: str
    url: str
    category: str
    region: str  # "israel" or "international"
    description: str = ""
    deadline: Optional[str] = None
    grant_amount: Optional[str] = None
    tags: list[str] = field(default_factory=list)
    scraped_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        return asdict(self)


class BaseScanner:
    """Base class for all scanners."""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(REQUEST_HEADERS)

    def fetch_page(self, url: str) -> Optional[BeautifulSoup]:
        """Fetch a web page and return parsed HTML."""
        for attempt in range(MAX_RETRIES + 1):
            try:
                response = self.session.get(url, timeout=REQUEST_TIMEOUT)
                response.raise_for_status()
                return BeautifulSoup(response.text, "lxml")
            except requests.RequestException as e:
                logger.warning(
                    "Attempt %d/%d failed for %s: %s",
                    attempt + 1,
                    MAX_RETRIES + 1,
                    url,
                    e,
                )
                if attempt < MAX_RETRIES:
                    time.sleep(RETRY_DELAY)
        logger.error("Failed to fetch %s after %d attempts", url, MAX_RETRIES + 1)
        return None

    def fetch_raw(self, url: str) -> Optional[str]:
        """Fetch raw content from a URL."""
        for attempt in range(MAX_RETRIES + 1):
            try:
                response = self.session.get(url, timeout=REQUEST_TIMEOUT)
                response.raise_for_status()
                return response.text
            except requests.RequestException as e:
                logger.warning(
                    "Attempt %d/%d failed for %s: %s",
                    attempt + 1,
                    MAX_RETRIES + 1,
                    url,
                    e,
                )
                if attempt < MAX_RETRIES:
                    time.sleep(RETRY_DELAY)
        return None

    def deep_scan_page(self, url: str) -> dict:
        """Fetch an individual call page and extract detailed content."""
        soup = self.fetch_page(url)
        if not soup:
            return {}

        info = {}

        # Try source-specific detail extractor first
        from scanners.extractors import get_detail_extractor
        detail_extractor = get_detail_extractor(url)
        if detail_extractor:
            info = detail_extractor(soup, url)
            if info.get("description"):
                return info

        # Generic detail extraction
        # 1. Get page title
        h1 = soup.select_one("h1")
        if h1:
            title = h1.get_text(strip=True)
            if title and len(title) > 5:
                info["page_title"] = title

        # 2. Get description from main content
        for sel in [
            "article .content", ".entry-content", ".post-content",
            ".field-name-body", ".main-content", "article", ".content-area",
            "#content", "main",
        ]:
            content_el = soup.select_one(sel)
            if content_el:
                paragraphs = content_el.select("p")
                desc_parts = []
                for p in paragraphs[:6]:
                    text = p.get_text(strip=True)
                    if text and len(text) > 30:
                        desc_parts.append(text)
                if desc_parts:
                    info["description"] = " ".join(desc_parts)[:500]
                    break

        # 3. Look for deadline
        if "deadline" not in info:
            deadline_keywords_he = ["מועד אחרון", "תאריך אחרון", "הגשה עד", "עד ליום", "דדליין"]
            deadline_keywords_en = ["deadline", "due date", "closing date", "submit by"]
            all_keywords = deadline_keywords_he + deadline_keywords_en
            for tag in soup.find_all(["span", "div", "p", "td", "li"]):
                text = tag.get_text(strip=True)
                if any(kw in text.lower() for kw in all_keywords):
                    match = re.search(r"(\d{1,2}[/.]\d{1,2}[/.]\d{2,4})", text)
                    if match:
                        info["deadline"] = match.group(1)
                        break

        # 4. Look for grant amount
        if "grant_amount" not in info:
            for tag in soup.find_all(["span", "div", "p", "td", "li"]):
                text = tag.get_text(strip=True)
                if any(c in text for c in ["₪", "$", "€", "ש\"ח"]):
                    amount_match = re.search(
                        r"[\$€₪][\d,.]+|[\d,.]+\s*(?:₪|ש\"ח|\$|€|USD|EUR)",
                        text,
                    )
                    if amount_match:
                        info["grant_amount"] = amount_match.group(0)
                        break

        return info

    def scan(self) -> list[CallForProposal]:
        """Override in subclasses to perform scanning."""
        raise NotImplementedError
