# Hopa - סורק קולות קוראים / Voice Scanner

כלי לסריקת קולות קוראים והזדמנויות הגשה מישראל ומהעולם, עם תזמון סריקה יומית אוטומטית.

A tool for scanning calls for proposals, grants, and submission opportunities from Israel and worldwide, with automatic daily scheduling.

## מקורות (34 סה"כ) / Sources

### ישראל (22 מקורות) / Israel
| # | מקור | תחום |
|---|------|------|
| 1 | אתר התמיכות הממשלתי - משרד האוצר | ממשלתי |
| 2 | משרד הפנים - קולות קוראים לרשויות | ממשלתי |
| 3 | משרד החינוך - קולות קוראים | חינוך |
| 4 | רשות החדשנות | חדשנות |
| 5 | ערב רב - קולות קוראים | תרבות |
| 6 | קרן ליוצרים עצמאיים - משרד התרבות | תרבות |
| 7 | קרן יהושע רבינוביץ לאמנויות | תרבות |
| 8 | קרן פלומס לאמנות | אמנות |
| 9 | המקרר - קולות קוראים | אמנות |
| 10 | איגוד מנהלי תרבות ברשויות המקומיות | תרבות |
| 11 | איגוד הבמאיות והבמאים | קולנוע |
| 12 | הפורום הדוקומנטרי | קולנוע |
| 13 | קרן גשר לקולנוע רב תרבותי | קולנוע |
| 14 | שתיל - קרנות וקולות קוראים | חברה |
| 15 | SocialMap - הקול קורה | חברה |
| 16 | חיים וסביבה - קולות קוראים | חברה |
| 17 | משאבים - מענקים לעמותות | עמותות |
| 18 | גיידסטאר - קולות קוראים לתמיכה | עמותות |
| 19 | אטלס - מענקים לרשויות מקומיות | ממשלתי |
| 20 | שח"ם - ארגון השחקנים | תרבות |
| 21 | הטכניון - קולות קוראים פעילים | מחקר |
| 22 | החטיבה להתיישבות | ממשלתי |

### בינלאומי (12 מקורות) / International
| # | Source | Category |
|---|--------|----------|
| 1 | Grants.gov RSS Feed | Government |
| 2 | Grants.gov API (Arts/Culture) | Arts |
| 3 | NIH Funding Opportunities RSS | Research |
| 4 | National Endowment for the Arts | Arts |
| 5 | Artwork Archive - Grants & Opportunities | Arts |
| 6 | Colossal - Artist Opportunities | Arts |
| 7 | San Francisco Arts Commission | Arts |
| 8 | fundsforNGOs - Arts & Culture | Culture |
| 9 | fundsforNGOs - Latest Grants | NGO |
| 10 | EU Funding Portal - Arts | Culture |
| 11 | Artenda - Project Grants | Arts |
| 12 | TransArtists - Funding Worldwide | Arts |

## התקנה / Installation

```bash
pip install -r requirements.txt
```

## שימוש / Usage

### סריקה חד-פעמית / One-time scan
```bash
python scanner.py                    # Scan all sources
python scanner.py --region israel    # Israeli sources only
python scanner.py --region intl      # International sources only
python scanner.py --category culture # Filter by category
python scanner.py --save --output both  # Save as JSON + CSV
```

### סריקה יומית אוטומטית / Automatic daily scanning
```bash
python scheduler.py                  # Start daily scanner (default 08:00)
python scheduler.py --time 09:00     # Custom time
python scheduler.py --now            # Scan now + schedule daily
python scheduler.py --now -v         # Verbose mode
```

## קטגוריות / Categories

| Category | Description |
|----------|-------------|
| `government` | ממשלתי / Government |
| `innovation` | חדשנות / Innovation & Tech |
| `education` | חינוך / Education |
| `culture` | תרבות / Culture |
| `arts` | אמנות / Arts |
| `film` | קולנוע / Film |
| `social` | חברה / Social Change |
| `ngo` | עמותות / NGOs |
| `research` | מחקר / Research |

## הוספת מקורות / Adding Sources

```python
# config.py
ISRAELI_SOURCES.append({
    "name": "שם המקור",
    "name_en": "Source Name",
    "url": "https://example.com/calls",
    "type": "html",  # html, rss, or api
    "category": "culture",
})
```
