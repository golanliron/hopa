"""
Source-specific extractors for Israeli calls for proposals.
Each extractor knows the HTML structure of a specific website.
"""

import logging
import re
from urllib.parse import urljoin

from bs4 import Tag

logger = logging.getLogger(__name__)


def extract_innovation_authority(soup, source: dict) -> list[dict]:
    """Extract calls from innovationisrael.org.il - uses .document_item structure."""
    calls = []
    items = soup.select("a.document_item")
    for item in items:
        # Skip closed calls
        closed = item.select_one(".flood-text.close")
        if closed and "הסתיימה" in closed.get_text():
            continue

        title_el = item.select_one(".title_kol_kore span")
        title = title_el.get_text(strip=True) if title_el else ""

        dept_el = item.select_one(".departments_kol_kore p")
        department = dept_el.get_text(strip=True) if dept_el else ""

        deadline_el = item.select_one(".document_item_doc_date_kol_kore div")
        deadline = deadline_el.get_text(strip=True) if deadline_el else None

        href = item.get("href", "")
        url = urljoin(source["url"], href)

        if title:
            calls.append({
                "title": title,
                "url": url,
                "deadline": deadline,
                "department": department,
            })
    return calls


def extract_innovation_authority_detail(soup, url: str) -> dict:
    """Extract details from an individual Innovation Authority call page."""
    info = {}

    # Description from main content area
    content = soup.select_one(".field-name-body, .kol-kore-content, .entry-content, article .content")
    if content:
        # Get first few paragraphs as description
        paragraphs = content.select("p")
        desc_parts = []
        for p in paragraphs[:5]:
            text = p.get_text(strip=True)
            if text and len(text) > 20:
                desc_parts.append(text)
        info["description"] = " ".join(desc_parts)[:500]

    # Deadline
    for tag in soup.find_all(["div", "span", "p"]):
        text = tag.get_text(strip=True)
        if "מועד אחרון להגשה" in text:
            # Extract the date part
            match = re.search(r"(\d{1,2}[/.]\d{1,2}[/.]\d{2,4})", text)
            if match:
                info["deadline"] = match.group(1)
            else:
                info["deadline"] = text.replace("מועד אחרון להגשה", "").strip()[:50]
            break

    return info


def extract_education_ministry(soup, source: dict) -> list[dict]:
    """Extract calls from pob.education.gov.il."""
    calls = []
    # The site uses Knockout.js for dynamic content, but has static links
    links = soup.select("a[href]")
    for link in links:
        href = link.get("href", "")
        title = link.get_text(strip=True)
        if not title or len(title) < 10:
            continue
        # Skip navigation links
        if href.startswith("/umbraco") or href.startswith("#"):
            continue
        if "/kolotkorim/" in href and href != "/kolotkorim/kolkore/":
            url = urljoin(source["url"], href)
            calls.append({
                "title": title,
                "url": url,
                "deadline": None,
            })
    return calls


def extract_education_detail(soup, url: str) -> dict:
    """Extract details from an education ministry call page."""
    info = {}
    # Try to find description
    content = soup.select_one(".content-wrapper, .main-content, article, .field-items")
    if content:
        text = content.get_text(strip=True)[:500]
        info["description"] = text

    # Try to find deadline
    for tag in soup.find_all(["span", "div", "p", "td"]):
        text = tag.get_text(strip=True)
        if any(kw in text for kw in ["מועד אחרון", "תאריך אחרון", "הגשה עד"]):
            match = re.search(r"(\d{1,2}[/.]\d{1,2}[/.]\d{2,4})", text)
            if match:
                info["deadline"] = match.group(1)
                break
    return info


def extract_btl(soup, source: dict) -> list[dict]:
    """Extract calls from btl.gov.il (Bituach Leumi)."""
    calls = []
    # Look for links in content area
    content = soup.select_one("#ContentPlaceHolder_Content, .content-area, #mainContent")
    if not content:
        content = soup

    links = content.select("a[href]")
    for link in links:
        title = link.get_text(strip=True)
        href = link.get("href", "")
        if not title or len(title) < 10:
            continue
        if any(kw in title for kw in ["קול קורא", "מענק", "תכנית", "קרן", "מסלול"]):
            url = urljoin(source["url"], href)
            calls.append({
                "title": title,
                "url": url,
                "deadline": None,
            })
    return calls


def extract_shatil(soup, source: dict) -> list[dict]:
    """Extract calls from shatil.org.il - uses loop-item structure with /kol/ links."""
    calls = []
    items = soup.select("a.loop-item.kol, a.loop-item--general[href*='/kol/']")
    if not items:
        # Fallback: all links to /kol/ pages
        items = soup.select("a[href*='/kol/']")

    seen_hrefs = set()
    for item in items:
        href = item.get("href", "")
        if not href or href in seen_hrefs:
            continue
        seen_hrefs.add(href)

        # Extract deadline from .date__deadline
        deadline_el = item.select_one(".date__deadline")
        deadline = deadline_el.get_text(strip=True) if deadline_el else None
        if deadline and deadline == "אין דדליין":
            deadline = None

        # Extract title from heading
        title_el = item.select_one("h3, h2, .info-wrap h3, .info-wrap h2")
        if title_el:
            title = title_el.get_text(strip=True)
        else:
            # Parse from full text: skip "דדליין" and date parts
            full_text = item.get_text(strip=True)
            title = re.sub(r"^דדליין[\d./\s]*(?:אין דדליין)?", "", full_text).strip()
            # Remove funder name at the end if present
            title = title[:150]

        # Extract funder/source
        funder_el = item.select_one(".kol_source, .source, .funder")
        funder = funder_el.get_text(strip=True) if funder_el else ""

        if title and len(title) > 5:
            url = urljoin(source["url"], href)
            calls.append({
                "title": title,
                "url": url,
                "description": funder,
                "deadline": deadline,
            })
    return calls


def extract_erev_rav(soup, source: dict) -> list[dict]:
    """Extract calls from erev-rav.com."""
    calls = []
    articles = soup.select("article, .post")
    for article in articles:
        title_el = article.select_one("h2 a, .entry-title a, h3 a")
        if not title_el:
            title_el = article.select_one("a[href]")
        if not title_el:
            continue

        title = title_el.get_text(strip=True)
        href = title_el.get("href", "")
        if not title or len(title) < 5:
            continue

        desc_el = article.select_one(".entry-content, .excerpt, .post-content, p")
        description = desc_el.get_text(strip=True)[:300] if desc_el else ""

        # Look for date
        date_el = article.select_one("time, .date, .post-date, .entry-date")
        date = date_el.get_text(strip=True) if date_el else None

        url = urljoin(source["url"], href)
        calls.append({
            "title": title,
            "url": url,
            "description": description,
            "deadline": date,
        })
    return calls


def extract_guidestar(soup, source: dict) -> list[dict]:
    """Extract calls from guidestar.org.il."""
    calls = []
    items = soup.select(".announcement-item, .search-result-item, .card, article, .item")
    for item in items:
        title_el = item.select_one("h2, h3, h4, .title, a")
        if not title_el:
            continue
        title = title_el.get_text(strip=True)
        link_el = item.select_one("a[href]")
        href = link_el.get("href", "") if link_el else ""
        if not title or len(title) < 5:
            continue

        desc_el = item.select_one(".description, .summary, p")
        description = desc_el.get_text(strip=True)[:300] if desc_el else ""

        url = urljoin(source["url"], href) if href else source["url"]
        calls.append({
            "title": title,
            "url": url,
            "description": description,
            "deadline": None,
        })
    return calls


def extract_atlas_grants(soup, source: dict) -> list[dict]:
    """Extract calls from atlas-grants.com."""
    calls = []
    items = soup.select("article, .post, .grant-item, .card, .entry")
    for item in items:
        title_el = item.select_one("h2 a, h3 a, .entry-title a, .card-title a")
        if not title_el:
            title_el = item.select_one("h2, h3, .title")
        if not title_el:
            continue
        title = title_el.get_text(strip=True)
        link_el = item.select_one("a[href]")
        href = link_el.get("href", "") if link_el else ""
        if not title or len(title) < 5:
            continue

        desc_el = item.select_one(".entry-content, .excerpt, p, .card-text")
        description = desc_el.get_text(strip=True)[:300] if desc_el else ""

        url = urljoin(source["url"], href) if href else source["url"]
        calls.append({
            "title": title,
            "url": url,
            "description": description,
            "deadline": None,
        })
    return calls


def extract_mashabim(soup, source: dict) -> list[dict]:
    """Extract calls from mashabim.org."""
    calls = []
    items = soup.select("article, .post, .entry, .card")
    for item in items:
        title_el = item.select_one("h2 a, h3 a, .entry-title a")
        if not title_el:
            continue
        title = title_el.get_text(strip=True)
        href = title_el.get("href", "")
        if not title or len(title) < 5:
            continue

        desc_el = item.select_one(".entry-content, .excerpt, p")
        description = desc_el.get_text(strip=True)[:300] if desc_el else ""

        url = urljoin(source["url"], href)
        calls.append({
            "title": title,
            "url": url,
            "description": description,
            "deadline": None,
        })
    return calls


def extract_socialmap(soup, source: dict) -> list[dict]:
    """Extract calls from socialmap.org.il."""
    calls = []
    items = soup.select(".call-item, .grant-item, article, .card, .post, .item")
    for item in items:
        title_el = item.select_one("h2, h3, h4, .title, a")
        if not title_el:
            continue
        title = title_el.get_text(strip=True)
        link_el = item.select_one("a[href]")
        href = link_el.get("href", "") if link_el else ""
        if not title or len(title) < 5:
            continue

        desc_el = item.select_one(".description, .summary, p, .excerpt")
        description = desc_el.get_text(strip=True)[:300] if desc_el else ""

        # Look for deadline
        deadline = None
        for tag in item.find_all(["span", "div", "p"]):
            text = tag.get_text(strip=True)
            if any(kw in text for kw in ["מועד", "תאריך", "עד"]):
                match = re.search(r"(\d{1,2}[/.]\d{1,2}[/.]\d{2,4})", text)
                if match:
                    deadline = match.group(1)
                    break

        url = urljoin(source["url"], href) if href else source["url"]
        calls.append({
            "title": title,
            "url": url,
            "description": description,
            "deadline": deadline,
        })
    return calls


def extract_mof_tmichot(soup, source: dict) -> list[dict]:
    """Extract calls from tmichot.mof.gov.il (Treasury support site)."""
    calls = []
    items = soup.select(".call-item, .proposal-item, article, .card, tr, .row-item, .list-item")
    for item in items:
        title_el = item.select_one("h2, h3, h4, .title, a, td:first-child")
        if not title_el:
            continue
        title = title_el.get_text(strip=True)
        link_el = item.select_one("a[href]")
        href = link_el.get("href", "") if link_el else ""
        if not title or len(title) < 5:
            continue

        url = urljoin(source["url"], href) if href else source["url"]
        calls.append({
            "title": title,
            "url": url,
            "deadline": None,
        })
    return calls


# Map source URLs to their specific extractors
SOURCE_EXTRACTORS = {
    "innovationisrael.org.il/kol_kore": extract_innovation_authority,
    "pob.education.gov.il": extract_education_ministry,
    "btl.gov.il": extract_btl,
    "shatil.org.il": extract_shatil,
    "erev-rav.com": extract_erev_rav,
    "guidestar.org.il": extract_guidestar,
    "atlas-grants.com": extract_atlas_grants,
    "mashabim.org": extract_mashabim,
    "socialmap.org.il": extract_socialmap,
    "tmichot.mof.gov.il": extract_mof_tmichot,
}

DETAIL_EXTRACTORS = {
    "innovationisrael.org.il": extract_innovation_authority_detail,
    "pob.education.gov.il": extract_education_detail,
}


def get_extractor(url: str):
    """Find a source-specific extractor for a URL."""
    for pattern, extractor in SOURCE_EXTRACTORS.items():
        if pattern in url:
            return extractor
    return None


def get_detail_extractor(url: str):
    """Find a detail page extractor for a URL."""
    for pattern, extractor in DETAIL_EXTRACTORS.items():
        if pattern in url:
            return extractor
    return None
