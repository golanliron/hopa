"""
Configuration for Hopa - Voice Scanner (סורק קולות קוראים)
Scanning calls for proposals from Israel and worldwide.
"""

# Israeli sources
ISRAELI_SOURCES = [
    {
        "name": "רשות החדשנות - קולות קוראים",
        "name_en": "Israel Innovation Authority - Calls for Proposals",
        "url": "https://innovationisrael.org.il/en/page/calls-proposals",
        "type": "html",
        "category": "innovation",
    },
    {
        "name": "שתיל - קרנות וקולות קוראים",
        "name_en": "Shatil - Grants & Calls",
        "url": "https://shatil.org.il/%D7%A7%D7%A8%D7%A0%D7%95%D7%AA-%D7%95%D7%A7%D7%95%D7%9C%D7%95%D7%AA-%D7%A7%D7%95%D7%A8%D7%90%D7%99%D7%9D/",
        "type": "html",
        "category": "social",
    },
    {
        "name": "מועצת הפיס לתרבות ולאמנות",
        "name_en": "Mifal HaPais Council for Culture & Arts",
        "url": "https://www.erev-rav.com/archives/tag/%D7%A7%D7%95%D7%9C-%D7%A7%D7%95%D7%A8%D7%90",
        "type": "html",
        "category": "culture",
    },
    {
        "name": "איגוד הבמאיות והבמאים - קולות קוראים",
        "name_en": "Directors Guild - Calls for Proposals",
        "url": "https://directorsguild.org.il/%D7%A7%D7%95%D7%9C%D7%95%D7%AA-%D7%A7%D7%95%D7%A8%D7%90%D7%99%D7%9D/%D7%A7%D7%95%D7%9C%D7%95%D7%AA-%D7%A7%D7%95%D7%A8%D7%90%D7%99%D7%9D/",
        "type": "html",
        "category": "film",
    },
    {
        "name": "משאבים - מענקים לעמותות",
        "name_en": "Mashabim - Grants for NGOs",
        "url": "https://mashabim.org/main-page/",
        "type": "html",
        "category": "ngo",
    },
]

# International sources
INTERNATIONAL_SOURCES = [
    {
        "name": "Grants.gov RSS",
        "url": "https://www.grants.gov/rss/GG_NewOppByCategory.xml",
        "type": "rss",
        "category": "government",
    },
    {
        "name": "fundsforNGOs - Arts & Culture",
        "url": "https://www2.fundsforngos.org/category/arts-culture/",
        "type": "html",
        "category": "culture",
    },
    {
        "name": "EU Funding Portal - Arts",
        "url": "https://eufundingportal.eu/tag/arts/",
        "type": "html",
        "category": "culture",
    },
    {
        "name": "Artenda - Project Grants",
        "url": "https://artenda.net/art-open-call-opportunity/project-grant",
        "type": "html",
        "category": "arts",
    },
    {
        "name": "TransArtists - Funding Worldwide",
        "url": "https://www.transartists.org/en/funding-worldwide",
        "type": "html",
        "category": "arts",
    },
    {
        "name": "Colossal - Artist Opportunities",
        "url": "https://www.thisiscolossal.com/category/opportunities/",
        "type": "html",
        "category": "arts",
    },
]

# Scanner settings
REQUEST_TIMEOUT = 15  # seconds
REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Hopa Grant Scanner; +https://github.com/golanliron/hopa)",
    "Accept-Language": "he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7",
}
MAX_RETRIES = 2
RETRY_DELAY = 3  # seconds

# Output settings
OUTPUT_DIR = "outputs"
OUTPUT_FORMAT = "json"  # json, csv, or both
