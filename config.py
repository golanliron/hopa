"""
Configuration for Hopa - Voice Scanner (סורק קולות קוראים)
Focused on: youth at risk, social mobility, education, marginalized communities,
tech innovation, dropout prevention, and special communities.
"""

# ============================================================
# Focus topics / נושאי מיקוד
# ============================================================
FOCUS_TOPICS = [
    "נוער בסיכון",
    "צעירים בסיכון",
    "מוביליות חברתית",
    "קהילות מודרות",
    "חדשנות טכנולוגית",
    "חינוך",
    "מניעת נשירה",
    "קהילות מיוחדות",
    "צעירים להשכלה",
    "youth at risk",
    "at-risk youth",
    "social mobility",
    "marginalized communities",
    "dropout prevention",
    "education innovation",
    "underserved communities",
]

# ============================================================
# Israeli sources (28)
# ============================================================
ISRAELI_SOURCES = [
    # ==========================================
    # ממשלתי / Government
    # ==========================================
    {
        "name": "אתר התמיכות הממשלתי - משרד האוצר",
        "name_en": "Government Support Site - Ministry of Finance",
        "url": "https://tmichot.mof.gov.il/call-for-proposals/",
        "type": "html",
        "category": "government",
        "topics": ["נוער בסיכון", "חינוך", "קהילות מודרות"],
    },
    {
        "name": "משרד הפנים - קולות קוראים לרשויות",
        "name_en": "Ministry of Interior - Calls for Local Authorities",
        "url": "https://www.gov.il/he/Departments/DynamicCollectors/kolkore-list",
        "type": "html",
        "category": "government",
        "topics": ["קהילות מיוחדות", "מוביליות חברתית"],
    },
    {
        "name": "רשות החדשנות - קולות קוראים",
        "name_en": "Israel Innovation Authority - Calls for Proposals",
        "url": "https://innovationisrael.org.il/kol_kore/",
        "type": "html",
        "category": "innovation",
        "topics": ["חדשנות טכנולוגית"],
    },
    {
        "name": "רשות החדשנות - טכנולוגיות למידה מותאמת אישית",
        "name_en": "Innovation Authority - Personalized Education Tech",
        "url": "https://innovationisrael.org.il/kol_kore/personalized-education-tech/",
        "type": "html",
        "category": "innovation",
        "topics": ["חדשנות טכנולוגית", "חינוך"],
    },
    {
        "name": "אטלס - מענקים לרשויות מקומיות",
        "name_en": "Atlas Grants - Local Authority Grants",
        "url": "https://atlas-grants.com/getgrants/",
        "type": "html",
        "category": "government",
        "topics": ["קהילות מודרות", "מוביליות חברתית"],
    },
    # ==========================================
    # חינוך ומניעת נשירה / Education & Dropout Prevention
    # ==========================================
    {
        "name": "משרד החינוך - קולות קוראים",
        "name_en": "Ministry of Education - Calls for Proposals",
        "url": "https://pob.education.gov.il/kolotkorim/kolkore/",
        "type": "html",
        "category": "education",
        "topics": ["חינוך", "מניעת נשירה", "נוער בסיכון"],
    },
    {
        "name": "משרד החינוך - קידום נוער (היל\"ה)",
        "name_en": "Ministry of Education - Youth Advancement (HILA)",
        "url": "https://pob.education.gov.il/municipal-services/main-youth-at-risk/youth-promotion-info/",
        "type": "html",
        "category": "education",
        "topics": ["נוער בסיכון", "מניעת נשירה", "צעירים בסיכון"],
    },
    {
        "name": "המדען הראשי במשרד החינוך - מחקר חינוכי",
        "name_en": "Chief Scientist MOE - Educational Research",
        "url": "https://chief-scientist.education.gov.il/kol-kore/",
        "type": "html",
        "category": "education",
        "topics": ["חינוך", "חדשנות טכנולוגית"],
    },
    {
        "name": "מינהל חדשנות וטכנולוגיה - משרד החינוך",
        "name_en": "Innovation & Tech Admin - MOE (EducAItion)",
        "url": "https://edu-tech.education.gov.il/taknot/kol-kore/educaition/",
        "type": "html",
        "category": "education",
        "topics": ["חדשנות טכנולוגית", "חינוך"],
    },
    {
        "name": "שפ\"י - שירות פסיכולוגי ייעוצי - קולות קוראים",
        "name_en": "SHEFI - Psychological Counseling Service",
        "url": "https://shefi.education.gov.il/publication/voices-calling/",
        "type": "html",
        "category": "education",
        "topics": ["נוער בסיכון", "מניעת נשירה"],
    },
    # ==========================================
    # נוער בסיכון וצעירים / Youth at Risk
    # ==========================================
    {
        "name": "ביטוח לאומי - קרנות (שפר) - קולות קוראים",
        "name_en": "National Insurance - Funds (SHEFER) - Calls",
        "url": "https://www.ezvonot.com/%D7%A7%D7%95%D7%9C%D7%95%D7%AA-%D7%A7%D7%95%D7%A8%D7%90%D7%99%D7%9D-%D7%A7%D7%A8%D7%A0%D7%95%D7%AA-%D7%94%D7%91%D7%99%D7%98%D7%95%D7%97-%D7%94%D7%9C%D7%90%D7%95%D7%9E%D7%99-2/",
        "type": "html",
        "category": "youth_at_risk",
        "topics": ["נוער בסיכון", "צעירים בסיכון", "קהילות מודרות"],
    },
    {
        "name": "ביטוח לאומי - קרן לילדים ונוער בסיכון",
        "name_en": "National Insurance - Children & Youth at Risk Fund",
        "url": "https://www.btl.gov.il/About/news/Pages/ArchiveFolder/kolKoreYeladim.aspx",
        "type": "html",
        "category": "youth_at_risk",
        "topics": ["נוער בסיכון", "צעירים בסיכון"],
    },
    {
        "name": "ביטוח לאומי - קול קורא רב-תחומי מסלול גמיש 2026",
        "name_en": "National Insurance - Multidisciplinary Flexible Track 2026",
        "url": "https://www.btl.gov.il/Funds/kolotkorim/kolotKorimList/KKGamishSiud2026-M.pdf",
        "type": "html",
        "category": "youth_at_risk",
        "topics": ["נוער בסיכון", "קהילות מודרות", "מוביליות חברתית"],
    },
    # ==========================================
    # מוביליות חברתית וקהילות / Social Mobility & Communities
    # ==========================================
    {
        "name": "הג'וינט - קידום מוביליות חברתית",
        "name_en": "JDC Israel - Social Mobility",
        "url": "https://www.thejoint.org.il/challenges/social_mobility/",
        "type": "html",
        "category": "social_mobility",
        "topics": ["מוביליות חברתית", "קהילות מודרות"],
    },
    {
        "name": "ג'וינט-אשלים - נוער וצעירים בסיכון",
        "name_en": "JDC-Ashalim - Youth at Risk",
        "url": "https://www.thejoint.org.il/",
        "type": "html",
        "category": "youth_at_risk",
        "topics": ["נוער בסיכון", "צעירים בסיכון", "קהילות מודרות"],
    },
    {
        "name": "קרן גנדיר - חינוך והשכלה גבוהה",
        "name_en": "Gandyr Foundation - Education & Higher Ed",
        "url": "https://www.gandyr.com/",
        "type": "html",
        "category": "education",
        "topics": ["צעירים להשכלה", "מוביליות חברתית", "מניעת נשירה"],
    },
    {
        "name": "יד הנדיב - חינוך וחברה",
        "name_en": "Yad Hanadiv - Education & Society",
        "url": "https://www.yadhanadiv.org.il/",
        "type": "html",
        "category": "education",
        "topics": ["חינוך", "מוביליות חברתית"],
    },
    {
        "name": "הכוורת - מקורות מימון למיזמים חברתיים",
        "name_en": "HaKaveret - Social Venture Funding Sources",
        "url": "https://hackaveret.org/knowledges/fund-raising/",
        "type": "html",
        "category": "social_mobility",
        "topics": ["חדשנות טכנולוגית", "מוביליות חברתית", "קהילות מודרות"],
    },
    {
        "name": "התוכנית למובילי לכידות חברתית",
        "name_en": "Social Cohesion Leaders Program",
        "url": "https://www.sci.org.il/",
        "type": "html",
        "category": "social_mobility",
        "topics": ["מוביליות חברתית", "קהילות מיוחדות"],
    },
    # ==========================================
    # חברה אזרחית ועמותות / Civil Society & NGOs
    # ==========================================
    {
        "name": "שתיל - קרנות וקולות קוראים",
        "name_en": "Shatil - Grants & Calls",
        "url": "https://shatil.org.il/%D7%A7%D7%A8%D7%A0%D7%95%D7%AA-%D7%95%D7%A7%D7%95%D7%9C%D7%95%D7%AA-%D7%A7%D7%95%D7%A8%D7%90%D7%99%D7%9D/",
        "type": "html",
        "category": "social",
        "topics": ["קהילות מודרות", "מוביליות חברתית", "נוער בסיכון"],
    },
    {
        "name": "SocialMap - הקול קורה",
        "name_en": "SocialMap - HaKol Kore",
        "url": "https://socialmap.org.il/hakol-kore",
        "type": "html",
        "category": "social",
        "topics": ["נוער בסיכון", "קהילות מודרות", "חינוך"],
    },
    {
        "name": "משאבים - מענקים לעמותות",
        "name_en": "Mashabim - Grants for NGOs",
        "url": "https://mashabim.org/main-page/",
        "type": "html",
        "category": "ngo",
        "topics": ["נוער בסיכון", "חינוך", "קהילות מיוחדות"],
    },
    {
        "name": "גיידסטאר - קולות קוראים לתמיכה (סעיף 3א)",
        "name_en": "GuideStar Israel - Government Support Calls",
        "url": "https://www.guidestar.org.il/search-announcements",
        "type": "html",
        "category": "ngo",
        "topics": ["נוער בסיכון", "חינוך", "קהילות מודרות"],
    },
    {
        "name": "ערב רב - קולות קוראים",
        "name_en": "Erev Rav - Calls for Proposals",
        "url": "https://www.erev-rav.com/archives/category/%D7%A7%D7%95%D7%9C-%D7%A7%D7%95%D7%A8%D7%90",
        "type": "html",
        "category": "culture",
        "topics": ["קהילות מיוחדות", "קהילות מודרות"],
    },
    # ==========================================
    # קרנות פילנתרופיות / Philanthropic Funds
    # ==========================================
    {
        "name": "קרן שוסטרמן ישראל",
        "name_en": "Schusterman Foundation Israel",
        "url": "https://www.schusterman.org/",
        "type": "html",
        "category": "education",
        "topics": ["צעירים להשכלה", "מוביליות חברתית", "חינוך"],
    },
    {
        "name": "קרן רבינוביץ לאמנויות",
        "name_en": "Rabinovich Foundation for the Arts",
        "url": "https://www.rabinovichfoundation.org.il/",
        "type": "html",
        "category": "culture",
        "topics": ["קהילות מיוחדות"],
    },
    {
        "name": "קרן ליוצרים עצמאיים - משרד התרבות",
        "name_en": "Independent Creators Fund - Ministry of Culture",
        "url": "https://www.kerentarbut.co.il/",
        "type": "html",
        "category": "culture",
        "topics": ["קהילות מיוחדות"],
    },
]

# ============================================================
# International sources - US focus (20)
# ============================================================
INTERNATIONAL_SOURCES = [
    # ==========================================
    # US Federal - Youth at Risk & Education
    # ==========================================
    {
        "name": "OJJDP - Office of Juvenile Justice (Open Funding)",
        "url": "https://ojjdp.ojp.gov/funding/current",
        "type": "html",
        "category": "youth_at_risk",
        "topics": ["youth at risk", "at-risk youth", "dropout prevention"],
    },
    {
        "name": "CYFAR - Children, Youth & Families at Risk (USDA/NIFA)",
        "url": "https://www.nifa.usda.gov/grants/programs/children-youth-families-risk-cyfar",
        "type": "html",
        "category": "youth_at_risk",
        "topics": ["youth at risk", "at-risk youth", "underserved communities"],
    },
    {
        "name": "FYSB - Family & Youth Services Bureau (HHS)",
        "url": "https://acf.gov/fysb/grants/funding-opportunities",
        "type": "html",
        "category": "youth_at_risk",
        "topics": ["youth at risk", "at-risk youth"],
    },
    {
        "name": "National Dropout Prevention Center - Grants",
        "url": "https://dropoutprevention.org/grants/",
        "type": "html",
        "category": "education",
        "topics": ["dropout prevention", "education innovation"],
    },
    {
        "name": "Grants.gov - Youth & Education RSS",
        "url": "https://www.grants.gov/rss/GG_OppModByCategory.xml",
        "type": "rss",
        "category": "government",
        "topics": ["youth at risk", "education innovation"],
    },
    {
        "name": "Grants.gov API - Youth at Risk",
        "url": "https://api.grants.gov/v1/api/search2",
        "type": "api",
        "category": "youth_at_risk",
        "api_params": {
            "keywords": "youth at risk education dropout prevention",
            "oppStatuses": ["forecasted", "posted"],
        },
        "topics": ["youth at risk", "dropout prevention", "education innovation"],
    },
    {
        "name": "Grants.gov API - Social Mobility & Underserved",
        "url": "https://api.grants.gov/v1/api/search2",
        "type": "api",
        "category": "social_mobility",
        "api_params": {
            "keywords": "social mobility underserved communities education",
            "oppStatuses": ["forecasted", "posted"],
        },
        "topics": ["social mobility", "marginalized communities"],
    },
    {
        "name": "Economic Mobility Catalog - Dropout Prevention",
        "url": "https://catalog.results4america.org/programs/dropout-prevention-programs",
        "type": "html",
        "category": "education",
        "topics": ["dropout prevention", "social mobility"],
    },
    # ==========================================
    # US - Private Foundations & Youth Grants
    # ==========================================
    {
        "name": "Instrumentl - Grants for Youth Programs",
        "url": "https://www.instrumentl.com/browse-grants/grants-for-youth-programs",
        "type": "html",
        "category": "youth_at_risk",
        "topics": ["youth at risk", "education innovation"],
    },
    {
        "name": "GrantWatch - Youth & Children's Grants",
        "url": "https://www.grantwatch.com/grantnews/12-grants-for-youth-and-childrens-programs-you-can-apply-for/",
        "type": "html",
        "category": "youth_at_risk",
        "topics": ["youth at risk", "at-risk youth"],
    },
    {
        "name": "Opportunities for Youth",
        "url": "https://opportunitiesforyouth.org/",
        "type": "html",
        "category": "youth_at_risk",
        "topics": ["youth at risk", "education innovation"],
    },
    {
        "name": "Urban Awareness USA - Funding Opportunities",
        "url": "https://urbanawarenessusa.org/blog/",
        "type": "html",
        "category": "social_mobility",
        "topics": ["marginalized communities", "social mobility"],
    },
    # ==========================================
    # International NGO / Education Grants
    # ==========================================
    {
        "name": "fundsforNGOs - Youth & Adolescents",
        "url": "https://www2.fundsforngos.org/category/youth-adolescents/",
        "type": "html",
        "category": "youth_at_risk",
        "topics": ["youth at risk", "education innovation"],
    },
    {
        "name": "fundsforNGOs - Education",
        "url": "https://www2.fundsforngos.org/category/education/",
        "type": "html",
        "category": "education",
        "topics": ["education innovation", "dropout prevention"],
    },
    {
        "name": "fundsforNGOs - Latest Grants",
        "url": "https://www2.fundsforngos.org/category/latest-funds-for-ngos/",
        "type": "html",
        "category": "ngo",
        "topics": ["marginalized communities", "social mobility"],
    },
    {
        "name": "NIH Funding Opportunities RSS",
        "url": "https://grants.nih.gov/grants/guide/newsfeed/fundingopps.xml",
        "type": "rss",
        "category": "research",
        "topics": ["youth at risk"],
    },
    {
        "name": "National Endowment for the Arts - Grants",
        "url": "https://www.arts.gov/grants",
        "type": "html",
        "category": "arts",
        "topics": ["underserved communities"],
    },
    {
        "name": "EU Funding Portal - Education & Youth",
        "url": "https://eufundingportal.eu/tag/education/",
        "type": "html",
        "category": "education",
        "topics": ["education innovation", "youth at risk"],
    },
    {
        "name": "Artenda - Social Impact Grants",
        "url": "https://artenda.net/art-open-call-opportunity/project-grant",
        "type": "html",
        "category": "arts",
        "topics": ["underserved communities"],
    },
    {
        "name": "TransArtists - Funding Worldwide",
        "url": "https://www.transartists.org/en/funding-worldwide",
        "type": "html",
        "category": "arts",
        "topics": ["underserved communities"],
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
