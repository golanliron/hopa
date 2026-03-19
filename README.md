# Hopa - סורק קולות קוראים / Voice Scanner

סורק קולות קוראים ממוקד בנושאים: **נוער בסיכון, מוביליות חברתית, צעירים להשכלה, קהילות מודרות, חדשנות טכנולוגית, חינוך, מניעת נשירה, קהילות מיוחדות**.

47 מקורות (27 ישראל + 20 בינלאומי) עם סריקה יומית אוטומטית.

## מקורות ישראליים (27)

| # | מקור | תחום | נושאים |
|---|------|------|--------|
| 1 | אתר התמיכות הממשלתי - משרד האוצר | ממשלתי | נוער בסיכון, חינוך |
| 2 | משרד הפנים - קולות קוראים | ממשלתי | קהילות מיוחדות |
| 3 | רשות החדשנות - קולות קוראים | חדשנות | חדשנות טכנולוגית |
| 4 | רשות החדשנות - טכנולוגיות למידה | חדשנות | חדשנות טכנולוגית, חינוך |
| 5 | אטלס - מענקים לרשויות | ממשלתי | קהילות מודרות |
| 6 | משרד החינוך - קולות קוראים | חינוך | חינוך, מניעת נשירה, נוער בסיכון |
| 7 | משרד החינוך - קידום נוער (היל"ה) | חינוך | נוער בסיכון, מניעת נשירה |
| 8 | המדען הראשי - משרד החינוך | חינוך | חינוך, חדשנות טכנולוגית |
| 9 | מינהל חדשנות וטכנולוגיה - EducAItion | חינוך | חדשנות טכנולוגית, חינוך |
| 10 | שפ"י - שירות פסיכולוגי ייעוצי | חינוך | נוער בסיכון, מניעת נשירה |
| 11 | ביטוח לאומי - קרנות (שפר) | נוער בסיכון | נוער בסיכון, צעירים בסיכון |
| 12 | ביטוח לאומי - קרן ילדים ונוער | נוער בסיכון | נוער בסיכון |
| 13 | ביטוח לאומי - מסלול גמיש 2026 | נוער בסיכון | מוביליות חברתית |
| 14 | הג'וינט - מוביליות חברתית | מוביליות | מוביליות חברתית, קהילות מודרות |
| 15 | ג'וינט-אשלים - נוער וצעירים | נוער בסיכון | נוער בסיכון, צעירים בסיכון |
| 16 | קרן גנדיר | חינוך | צעירים להשכלה, מניעת נשירה |
| 17 | יד הנדיב | חינוך | חינוך, מוביליות חברתית |
| 18 | הכוורת - מימון מיזמים חברתיים | מוביליות | חדשנות, קהילות מודרות |
| 19 | התוכנית למובילי לכידות חברתית | מוביליות | מוביליות חברתית |
| 20 | שתיל - קרנות וקולות קוראים | חברה | קהילות מודרות, נוער בסיכון |
| 21 | SocialMap - הקול קורה | חברה | נוער בסיכון, חינוך |
| 22 | משאבים - מענקים לעמותות | עמותות | נוער בסיכון, חינוך |
| 23 | גיידסטאר - קולות קוראים | עמותות | נוער בסיכון, חינוך |
| 24 | ערב רב - קולות קוראים | תרבות | קהילות מיוחדות |
| 25 | קרן שוסטרמן | חינוך | צעירים להשכלה |
| 26 | קרן רבינוביץ | תרבות | קהילות מיוחדות |
| 27 | קרן ליוצרים עצמאיים | תרבות | קהילות מיוחדות |

## מקורות בינלאומיים (20)

| # | Source | Category | Topics |
|---|--------|----------|--------|
| 1 | OJJDP - Juvenile Justice | Youth at Risk | at-risk youth, dropout prevention |
| 2 | CYFAR - Children & Youth at Risk (USDA) | Youth at Risk | underserved communities |
| 3 | FYSB - Family & Youth Services (HHS) | Youth at Risk | at-risk youth |
| 4 | National Dropout Prevention Center | Education | dropout prevention |
| 5 | Grants.gov RSS | Government | youth, education |
| 6 | Grants.gov API - Youth at Risk | Youth at Risk | dropout prevention |
| 7 | Grants.gov API - Social Mobility | Social Mobility | marginalized communities |
| 8 | Economic Mobility Catalog | Education | dropout prevention, social mobility |
| 9 | Instrumentl - Youth Programs | Youth at Risk | education innovation |
| 10 | GrantWatch - Youth Grants | Youth at Risk | at-risk youth |
| 11 | Opportunities for Youth | Youth at Risk | education innovation |
| 12 | Urban Awareness USA | Social Mobility | marginalized communities |
| 13 | fundsforNGOs - Youth | Youth at Risk | education innovation |
| 14 | fundsforNGOs - Education | Education | dropout prevention |
| 15 | fundsforNGOs - Latest | NGO | social mobility |
| 16 | NIH Funding RSS | Research | youth at risk |
| 17 | NEA - Arts Grants | Arts | underserved communities |
| 18 | EU Funding Portal - Education | Education | youth at risk |
| 19 | Artenda - Social Impact | Arts | underserved communities |
| 20 | TransArtists - Worldwide | Arts | underserved communities |

## שימוש / Usage

```bash
# סריקה מלאה
python scanner.py

# סריקה לפי תחום
python scanner.py --category youth_at_risk
python scanner.py --category education
python scanner.py --category social_mobility

# סריקה לפי נושא
python scanner.py --topic "נוער בסיכון"
python scanner.py --topic "dropout prevention"

# סריקה יומית אוטומטית
python scheduler.py                  # כל יום ב-08:00
python scheduler.py --time 09:00     # שעה מותאמת
python scheduler.py --now            # סרוק עכשיו + תזמן יומי
```

## קטגוריות / Categories

| Category | תיאור |
|----------|--------|
| `youth_at_risk` | נוער/צעירים בסיכון |
| `education` | חינוך ומניעת נשירה |
| `social_mobility` | מוביליות חברתית |
| `innovation` | חדשנות טכנולוגית |
| `social` | חברה אזרחית |
| `ngo` | עמותות ומגזר שלישי |
| `government` | ממשלתי |
| `culture` | תרבות וקהילות מיוחדות |
| `arts` | אמנות |
| `research` | מחקר |
