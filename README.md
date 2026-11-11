# 📅 smartbuy · Category Seasonality App

An interactive **Streamlit + Plotly** web app that measures how seasonal each of an online shop's
**100 product categories** is, when it peaks, and which categories to plan campaigns for first.

Built as a group project in the *AI in Data Analytics* module of our Data Analytics bootcamp.

**Team:** Carlos Musetti · Lorenz Schneider · Majid  · Prasad Natuskar

---

## The problem

smartbuy's Content Department judged category seasonality **by eyeballing charts**: slow, subjective
and impossible to repeat. They had 100 CSV files (one per category) with monthly clicks for 2021 and
wanted a faster, more reliable answer to three questions:

1. **Which** categories are seasonal?
2. **When** do they peak?
3. **Which** ones deserve campaign planning first?

## The solution

A data pipeline turned into a self-service web app, so business users can explore the results
themselves instead of waiting for a slide deck.

| Step | What happens |
|---|---|
| **Combine** | 100 raw files → one table of 1,200 rows (100 categories × 12 months) |
| **Clean** | 30 missing months filled by *circular* interpolation (December and January count as neighbours) |
| **Measure** | Seasonality index = month ÷ category average · Score = max index − min index |
| **Classify** | Strength: flat (< 0.5), moderate (0.5–1.0), strong (> 1.0) · peak month mapped to a season |
| **Prioritise** | Split at the median size and median score → 4 priority groups |
| **Share** | Multipage Streamlit app with filters, rankings, deep dives and CSV downloads |

## Key findings

- **81 of 100** categories show a seasonal pattern (37 strong, 44 moderate); 19 are flat.
- **November** is the busiest month (10.6 % of all clicks) and the most common peak month (34 categories).
  **February** is the quietest (7.2 %).
- Winter (31) and autumn (29) peakers clearly outnumber spring (11) and summer (10).
- Most seasonal category: **ski & snowboard helmets**, peaking in January with **21×** the clicks of June.
- **25 categories are big & seasonal**: plan stock, content and campaigns for them 4–6 weeks before their peak.

## The app

| Page | What you can do |
|---|---|
| 🏠 **Project summary** | The challenge, the approach, data-driven key findings and recommendations |
| 📊 **KPIs** | Headline numbers, share of clicks per month, size × seasonality matrix, downloadable priority list |
| 🏆 **Top clicks** | Rank categories by clicks; choose *n* with a slider |
| 🌦️ **It's all about seasonality** | Season patterns, most seasonal categories, single-category deep dive, and the most similar categories by correlation |

A shared sidebar filters every page by season, strength and priority group.

## Project structure

```
├── app.py                  # entry point: theme, navigation, shared sidebar
├── ui.py                   # design system: CSS, KPI cards, chart styling, sidebar filters
├── utils.py                # data loading + KPI calculations (cached with st.cache_data)
├── views/                  # one file per page
│   ├── home.py
│   ├── kpis.py
│   ├── top_clicks.py
│   └── seasonality.py
├── data/
│   ├── combined_categories.csv   # what the app loads
│   └── raw/pis_1.csv … pis_100.csv
├── scripts/combine_data.py # rebuilds combined_categories.csv from data/raw
├── notebooks/app_production.ipynb  # step-by-step walkthrough of how the app was built
├── .streamlit/config.toml  # theme
└── requirements.txt
```

> The notebook documents the build process, including an earlier version of the page layout; the code
> in `views/` is the current version.

## Run it locally

```bash
git clone <this-repo-url>
cd smartbuy-seasonality-app
python -m venv .venv
# Windows: .venv\Scripts\activate   ·   macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

The app opens at <http://localhost:8501>. To rebuild the combined data file from the raw files:
`python scripts/combine_data.py`.

## Deploy

The repo is ready for [Streamlit Community Cloud](https://share.streamlit.io): connect the GitHub repo,
choose `app.py` as the main file, and deploy.

## Tech stack

Python · pandas · NumPy · Plotly Express · Streamlit (`st.navigation`, `st.cache_data`, session state, custom CSS)

## Disclaimer

This was a group project by **Carlos Musetti, Lorenz Schneider, Majid and Prasad Natuskar**.

The design and the code of this app were created with help from **Claude** (Anthropic's AI assistant).
We directed the project, made the analytical decisions, and reviewed, tested and adapted the AI-assisted
output. Responsibility for the final result and any remaining errors is ours.
