"""Base scanner class and data models."""

import logging
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

    def scan(self) -> list[CallForProposal]:
        """Override in subclasses to perform scanning."""
        raise NotImplementedError
