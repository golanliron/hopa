"""
Configuration for Hopa - Voice Scanner (סורק קולות קוראים)
Scanning calls for proposals from Israel and worldwide.
"""

# ============================================================
# Israeli sources (20+)
# ============================================================
ISRAELI_SOURCES = [
    # --- ממשלתי / Government ---
    {
        "name": "אתר התמיכות הממשלתי - משרד האוצר",
        "name_en": "Government Support Site - Ministry of Finance",
        "url": "https://tmichot.mof.gov.il/call-for-proposals/",
        "type": "html",
        "category": "government",
    },
    {
        "name": "משרד הפנים - קולות קוראים לרשויות",
        "name_en": "Ministry of Interior - Calls for Local Authorities",
        "url": "https://www.gov.il/he/Departments/DynamicCollectors/kolkore-list",
        "type": "html",
        "category": "government",
    },
    {
        "name": "משרד החינוך - קולות קוראים",
        "name_en": "Ministry of Education - Calls for Proposals",
        "url": "https://pob.education.gov.il/kolotkorim/kolkore/",
        "type": "html",
        "category": "education",
    },
    {
        "name": "רשות החדשנות - קולות קוראים",
        "name_en": "Israel Innovation Authority - Calls for Proposals",
        "url": "https://innovationisrael.org.il/en/page/calls-proposals",
        "type": "html",
        "category": "innovation",
    },
    # --- תרבות ואמנות / Culture & Arts ---
    {
        "name": "ערב רב - קולות קוראים",
        "name_en": "Erev Rav - Calls for Proposals",
        "url": "https://www.erev-rav.com/archives/category/%D7%A7%D7%95%D7%9C-%D7%A7%D7%95%D7%A8%D7%90",
        "type": "html",
        "category": "culture",
    },
    {
        "name": "קרן ליוצרים עצמאיים - משרד התרבות",
        "name_en": "Independent Creators Fund - Ministry of Culture",
        "url": "https://www.kerentarbut.co.il/",
        "type": "html",
        "category": "culture",
    },
    {
        "name": "קרן יהושע רבינוביץ לאמנויות",
        "name_en": "Rabinovich Foundation for the Arts",
        "url": "https://www.rabinovichfoundation.org.il/",
        "type": "html",
        "category": "culture",
    },
    {
        "name": "קרן פלומס לאמנות",
        "name_en": "Plumas Art Foundation",
        "url": "https://plumas.org.il/",
        "type": "html",
        "category": "arts",
    },
    {
        "name": "המקרר - קולות קוראים",
        "name_en": "HaMecarer Gallery - Open Calls",
        "url": "https://hamecarer.co.il/about/open-call/",
        "type": "html",
        "category": "arts",
    },
    {
        "name": "איגוד מנהלי תרבות ברשויות המקומיות",
        "name_en": "Association of Cultural Directors",
        "url": "https://www.association-of-cultural-directors.com/%D7%A7%D7%95%D7%9C%D7%95%D7%AA-%D7%A7%D7%95%D7%A8%D7%90%D7%99%D7%9D/",
        "type": "html",
        "category": "culture",
    },
    # --- קולנוע / Film ---
    {
        "name": "איגוד הבמאיות והבמאים - קולות קוראים",
        "name_en": "Directors Guild - Calls for Proposals",
        "url": "https://directorsguild.org.il/%D7%A7%D7%95%D7%9C%D7%95%D7%AA-%D7%A7%D7%95%D7%A8%D7%90%D7%99%D7%9D/%D7%A7%D7%95%D7%9C%D7%95%D7%AA-%D7%A7%D7%95%D7%A8%D7%90%D7%99%D7%9D/",
        "type": "html",
        "category": "film",
    },
    {
        "name": "הפורום הדוקומנטרי - קולות קוראים והגשות",
        "name_en": "Documentary Forum - Calls & Submissions",
        "url": "https://www.fdoc.org.il/all-submissions/",
        "type": "html",
        "category": "film",
    },
    {
        "name": "קרן גשר לקולנוע רב תרבותי",
        "name_en": "Gesher Multicultural Film Fund",
        "url": "https://gesherfilmfund.org.il/Page/6/",
        "type": "html",
        "category": "film",
    },
    # --- חברה וקהילה / Social ---
    {
        "name": "שתיל - קרנות וקולות קוראים",
        "name_en": "Shatil - Grants & Calls",
        "url": "https://shatil.org.il/%D7%A7%D7%A8%D7%A0%D7%95%D7%AA-%D7%95%D7%A7%D7%95%D7%9C%D7%95%D7%AA-%D7%A7%D7%95%D7%A8%D7%90%D7%99%D7%9D/",
        "type": "html",
        "category": "social",
    },
    {
        "name": "SocialMap - הקול קורה",
        "name_en": "SocialMap - HaKol Kore",
        "url": "https://socialmap.org.il/hakol-kore",
        "type": "html",
        "category": "social",
    },
    {
        "name": "חיים וסביבה - קולות קוראים",
        "name_en": "Life & Environment - Calls for Proposals",
        "url": "https://www.sviva.net/category/%D7%A7%D7%95%D7%9C%D7%95%D7%AA-%D7%A7%D7%95%D7%A8%D7%90%D7%99%D7%9D/",
        "type": "html",
        "category": "social",
    },
    # --- עמותות ומענקים / NGOs & Grants ---
    {
        "name": "משאבים - מענקים לעמותות",
        "name_en": "Mashabim - Grants for NGOs",
        "url": "https://mashabim.org/main-page/",
        "type": "html",
        "category": "ngo",
    },
    {
        "name": "גיידסטאר - קולות קוראים לתמיכה (סעיף 3א)",
        "name_en": "GuideStar Israel - Government Support Calls",
        "url": "https://www.guidestar.org.il/search-announcements",
        "type": "html",
        "category": "ngo",
    },
    {
        "name": "אטלס - מענקים לרשויות מקומיות",
        "name_en": "Atlas Grants - Local Authority Grants",
        "url": "https://atlas-grants.com/getgrants/",
        "type": "html",
        "category": "government",
    },
    {
        "name": "שח\"ם - ארגון השחקנים בישראל",
        "name_en": "SHAHAM - Actors Organization",
        "url": "https://www.shaham.org.il/%D7%97%D7%93%D7%A9%D7%95%D7%AA",
        "type": "html",
        "category": "culture",
    },
    # --- מחקר ואקדמיה / Research ---
    {
        "name": "הטכניון - קולות קוראים פעילים",
        "name_en": "Technion - Active Calls for Proposals",
        "url": "https://www.trdf.co.il/%D7%A7%D7%95%D7%9C%D7%95%D7%AA_%D7%A7%D7%95%D7%A8%D7%90%D7%99%D7%9D_%D7%A4%D7%A2%D7%99%D7%9C%D7%99%D7%9D/",
        "type": "html",
        "category": "research",
    },
    {
        "name": "החטיבה להתיישבות - קולות קוראים",
        "name_en": "Settlement Division - Calls for Proposals",
        "url": "https://www.hityashvut.org.il/%D7%A7%D7%95%D7%9C%D7%95%D7%AA-%D7%A7%D7%95%D7%A8%D7%90%D7%99%D7%9D/",
        "type": "html",
        "category": "government",
    },
]

# ============================================================
# International sources (US focus + worldwide)
# ============================================================
INTERNATIONAL_SOURCES = [
    # --- US Government / Federal ---
    {
        "name": "Grants.gov - All Opportunities RSS",
        "url": "https://www.grants.gov/rss/GG_OppModByCategory.xml",
        "type": "rss",
        "category": "government",
    },
    {
        "name": "Grants.gov - Arts (NEA) API",
        "url": "https://api.grants.gov/v1/api/search2",
        "type": "api",
        "category": "arts",
        "api_params": {
            "keywords": "arts culture",
            "oppStatuses": ["forecasted", "posted"],
        },
    },
    {
        "name": "NIH Funding Opportunities RSS",
        "url": "https://grants.nih.gov/grants/guide/newsfeed/fundingopps.xml",
        "type": "rss",
        "category": "research",
    },
    # --- US Arts & Culture ---
    {
        "name": "National Endowment for the Arts - Grants",
        "url": "https://www.arts.gov/grants",
        "type": "html",
        "category": "arts",
    },
    {
        "name": "Artwork Archive - Artist Grants & Opportunities",
        "url": "https://www.artworkarchive.com/call-for-entry/complete-guide-to-2026-artist-grants-opportunities",
        "type": "html",
        "category": "arts",
    },
    {
        "name": "Colossal - Artist Opportunities",
        "url": "https://www.thisiscolossal.com/category/opportunities/",
        "type": "html",
        "category": "arts",
    },
    {
        "name": "San Francisco Arts Commission - Grants",
        "url": "https://www.sfartscommission.org/content/grants",
        "type": "html",
        "category": "arts",
    },
    # --- International NGO / Grants ---
    {
        "name": "fundsforNGOs - Arts & Culture",
        "url": "https://www2.fundsforngos.org/category/arts-culture/",
        "type": "html",
        "category": "culture",
    },
    {
        "name": "fundsforNGOs - Latest Grants",
        "url": "https://www2.fundsforngos.org/category/latest-funds-for-ngos/",
        "type": "html",
        "category": "ngo",
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
]

# ============================================================
# Scanner settings
# ============================================================
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

# Scheduler settings
SCAN_INTERVAL_HOURS = 24  # scan once per day
SCAN_TIME = "08:00"  # daily scan time (HH:MM)
