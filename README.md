# Hopa - סורק קולות קוראים / Voice Scanner

כלי לסריקת קולות קוראים והזדמנויות הגשה מישראל ומהעולם.

A tool for scanning calls for proposals, grants, and submission opportunities from Israel and worldwide.

## מקורות / Sources

### ישראל / Israel
- רשות החדשנות (Israel Innovation Authority)
- שתיל - הקרן החדשה לישראל (Shatil)
- מועצת הפיס לתרבות ולאמנות (Mifal HaPais Council for Culture & Arts)
- איגוד הבמאיות והבמאים (Directors Guild)
- משאבים - מענקים לעמותות (Mashabim)

### בינלאומי / International
- Grants.gov (US Federal Grants - RSS)
- fundsforNGOs - Arts & Culture
- EU Funding Portal
- Artenda - Project Grants
- TransArtists - Funding Worldwide
- Colossal - Artist Opportunities

## התקנה / Installation

```bash
pip install -r requirements.txt
```

## שימוש / Usage

```bash
# Scan all sources
python scanner.py

# Scan Israeli sources only
python scanner.py --region israel

# Scan international sources only
python scanner.py --region intl

# Filter by category
python scanner.py --category culture

# Save results to file
python scanner.py --save --output json
python scanner.py --save --output csv
python scanner.py --save --output both

# Verbose mode
python scanner.py -v
```

## קטגוריות / Categories

| Category | Description |
|----------|-------------|
| `innovation` | חדשנות וטכנולוגיה / Innovation & Tech |
| `social` | שינוי חברתי / Social Change |
| `culture` | תרבות ואמנות / Culture & Arts |
| `film` | קולנוע / Film |
| `ngo` | עמותות / NGOs |
| `government` | ממשלתי / Government |
| `arts` | אמנות / Arts |

## הוספת מקורות / Adding Sources

ניתן להוסיף מקורות חדשים בקובץ `config.py`:

```python
ISRAELI_SOURCES.append({
    "name": "שם המקור",
    "name_en": "Source Name",
    "url": "https://example.com/calls",
    "type": "html",
    "category": "culture",
})
```
