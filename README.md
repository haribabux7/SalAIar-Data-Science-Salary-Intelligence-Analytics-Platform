[5.md](https://github.com/user-attachments/files/29463061/5.md)
# 💼 SalAIar — Data Science Salary Intelligence & Analytics Platform

> An end-to-end data analytics project that explores, cleans, models, and visualizes global Data Science salary trends from 2020 onward — built with Python, SQL, and Streamlit.

**SalAIar** (Salary + AI + Radar) is a portfolio-grade analytics project that turns a raw, multi-currency global salary dataset into a fully interactive intelligence dashboard. It answers the questions every data professional, recruiter, and hiring manager actually cares about: *Who earns what, where, at which experience level, and how is that changing year over year?*

The project follows the complete analytics lifecycle — **Raw Data → Cleaning → EDA → SQL Business Queries → Visualization → Interactive Dashboard** — and is structured so that each layer (Python notebooks, SQL scripts, Streamlit app) can be reviewed, reproduced, or extended independently.

---


---

## 📖 Overview

The Data Science job market is exploding in size, geography, and compensation diversity — but most public salary discussions rely on anecdote rather than data. **SalAIar** closes that gap.

- **Purpose** — Provide an honest, data-driven view of Data Science compensation across roles, countries, company sizes, experience levels, and remote-work configurations.
- **Business Value** — Helps recruiters benchmark offers, helps candidates negotiate confidently, and helps companies design competitive compensation bands.
- **User Benefit** — A single dashboard replaces hours of survey-reading with instant, filterable insights and downloadable slices of the dataset.
- **Main Functionality** — Cleans a raw multi-currency salary dataset, runs 30+ business SQL queries, performs EDA, and serves an interactive Streamlit dashboard with KPI cards, trend lines, geographic comparisons, and exportable views.

---

## ✨ Features

### Core Features
- ✅ Full data pipeline: Raw CSV → Cleaned CSV → SQL-ready dataset
- ✅ 30+ documented business SQL queries with insights & recommendations
- ✅ Interactive Streamlit dashboard with multi-dimensional filters
- ✅ KPI cards (Total Roles, Avg Salary, Max Salary, Remote %)
- ✅ Trend, distribution, geographic, and ranking visualizations

### User Features
- ✅ Filter by **work year** and **experience level**
- ✅ Toggle raw data table view
- ✅ One-click **CSV download** of filtered slice
- ✅ Responsive layout with side-by-side charts

### Analyst / Admin Features
- ✅ Reproducible Jupyter notebooks for cleaning, EDA, and visualization
- ✅ Standalone Python cleaning script for batch automation
- ✅ SQL scripts split into Cleaning / EDA / Business Queries

### Advanced Features
- ✅ Plotly-powered interactive charts (zoom, hover, export)
- ✅ Cached data loading for fast re-renders
- ✅ Cross-border employment analysis (residence vs. company location)
- ✅ Remote-work salary premium analysis

### Security & Quality Features
- ✅ No hard-coded credentials — environment-variable driven
- ✅ Input validation on all dashboard filters
- ✅ Read-only data access in the app layer
- ✅ Deterministic cleaning pipeline (reproducible outputs)

---

## 🧰 Tech Stack

### Frontend / Visualization
- **Streamlit** — interactive web app framework
- **Plotly Express & Graph Objects** — interactive charts
- **Matplotlib & Seaborn** — statistical plotting (notebooks)

### Backend / Data Processing
- **Python 3.10+**
- **Pandas** — data wrangling
- **NumPy** — numerical operations

### Database
- **MySQL / PostgreSQL** — SQL execution layer for business queries
- **SQLite** — lightweight local alternative

### Data Analytics
- **Jupyter Notebook** — EDA, cleaning, visualization
- **30+ SQL Business Queries** — documented with insights

### DevOps & Deployment
- **Streamlit Community Cloud** — primary deployment target
- **Render / Railway / AWS EC2** — alternative deployments
- **GitHub Actions** — CI for linting & smoke tests

### Development Tools
- **VS Code**, **JupyterLab**
- **Git & GitHub** — version control
- **pytest** — testing
- **Black & Flake8** — formatting & linting

---

## 🏗️ Architecture

```text
                ┌─────────────────────┐
                │   Raw_Data.csv      │
                └──────────┬──────────┘
                           │
                  ┌────────▼─────────┐
                  │ Data_Cleaning.py │  ◄── Python / Pandas
                  └────────┬─────────┘
                           │
                ┌──────────▼──────────┐
                │  Cleaned_Data.csv   │
                └─────┬───────────┬───┘
                      │           │
            ┌─────────▼──┐   ┌────▼─────────┐
            │ SQL Layer  │   │ EDA Notebooks│
            │ (Queries)  │   │ (Plots/Stats)│
            └─────────┬──┘   └────┬─────────┘
                      │           │
                      └─────┬─────┘
                            │
                ┌───────────▼────────────┐
                │  Streamlit Dashboard   │
                │  (Plotly + Filters)    │
                └───────────┬────────────┘
                            │
                       End Users
```

- **Client–Server Communication:** Streamlit handles state on the server; the browser receives rendered Plotly JSON for each interaction.
- **Database Relationships:** Single denormalized fact table `ds_salaries` with categorical dimensions (experience_level, employment_type, company_size, company_location, employee_residence).

---

## 📁 Project Structure

```text
salaiar/
│
└── Data-Analytics-Project/
    ├── Dataset/
    │   ├── Raw_Data.csv              # Source dataset (multi-currency)
    │   └── Cleaned_Data.csv          # Cleaned & normalized dataset
    │
    ├── Python/
    │   ├── Dashboard.py              # Streamlit interactive dashboard
    │   ├── Data_Cleaning.ipynb       # Notebook: cleaning walkthrough
    │   ├── Data_Cleaning_Script.py   # Reusable cleaning pipeline
    │   ├── Data_Visualization.ipynb  # Notebook: charts & insights
    │   ├── EDA.ipynb                 # Notebook: exploratory analysis
    │   └── Requirements.txt          # Python dependencies
    │
    ├── SQL/
    │   ├── Data_Cleaning.sql         # SQL cleaning statements
    │   ├── EDA.sql                   # Exploratory SQL queries
    │   └── Business_Queries.sql      # 30 business questions + insights
    │
    ├── docs/
    │   └── screenshots/              # Dashboard screenshots
    │
    └── README.md
```

---

## ⚙️ Installation

### Prerequisites
- Python **3.10+**
- pip / venv
- MySQL or PostgreSQL (optional — only for the SQL layer)
- Git

### Clone the Repository
```bash
git clone https://github.com/haribabux7/salaiar.git
cd salaiar/Data-Analytics-Project
```

### Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows
```

### Install Dependencies
```bash
pip install -r Python/Requirements.txt
```

### Configure Environment Variables
Create a `.env` file in the project root (see next section).

### Run the Dashboard
```bash
cd Python
streamlit run Dashboard.py
```
Open `http://localhost:8501` in your browser.

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
# App
PORT=8501
APP_ENV=development

# Database (optional — for SQL layer)
DATABASE_URL=postgresql://user:password@localhost:5432/ds_salaries
MYSQL_URI=mysql://user:password@localhost:3306/ds_salaries

# Auth (reserved for future admin features)
JWT_SECRET=replace-with-strong-secret
API_KEY=your-api-key

# Email (reserved for report delivery feature)
EMAIL_HOST=smtp.gmail.com
EMAIL_USER=you@example.com
EMAIL_PASSWORD=app-password
```

| Variable | Purpose |
|---|---|
| `PORT` | Streamlit server port |
| `APP_ENV` | `development` / `production` toggle |
| `DATABASE_URL` / `MYSQL_URI` | SQL connection string |
| `JWT_SECRET` | Token signing key (future auth) |
| `API_KEY` | External API integrations |
| `EMAIL_*` | SMTP credentials for scheduled reports |

---

## 🚀 Usage

1. **Explore** — open the dashboard, scan the four KPI cards for a market snapshot.
2. **Filter** — narrow by `work_year` and `experience_level` from the sidebar.
3. **Analyze** — inspect salary distributions, top-paying titles, and yearly trends.
4. **Export** — toggle "Show Raw Data" and click **Download Filtered Data** for offline analysis.
5. **Deep-dive** — open the Jupyter notebooks (`EDA.ipynb`, `Data_Visualization.ipynb`) for narrative analysis.
6. **Benchmark** — run `Business_Queries.sql` against the cleaned dataset for board-ready answers.

**Example scenarios**
- A recruiter validates a $145K offer for a Senior ML Engineer in Germany.
- A candidate compares remote vs on-site salary premiums before negotiation.
- A founder sizes a competitive comp band for a small EU-based data team.

---

## 🛠️ API / SQL Endpoints

Although this project is dashboard-first, the SQL layer functions as the analytical "API." Representative queries:

| Method | Endpoint / Query | Description |
|--------|------------------|-------------|
| GET | `SELECT AVG(salary_in_usd) FROM ds_salaries` | Overall average salary |
| GET | `SELECT experience_level, AVG(salary_in_usd) ... GROUP BY experience_level` | Salary by experience |
| GET | `SELECT work_year, AVG(salary_in_usd) ... GROUP BY work_year` | Yearly trend |
| GET | `SELECT company_location, AVG(salary_in_usd) ... LIMIT 5` | Top-paying countries |
| GET | `SELECT remote_ratio, AVG(salary_in_usd) ... GROUP BY remote_ratio` | Remote vs onsite |

**Example response (top countries):**
```json
[
  { "company_location": "US", "avg_salary_usd": 151822 },
  { "company_location": "CA", "avg_salary_usd": 99823 },
  { "company_location": "DE", "avg_salary_usd": 89134 }
]
```

---

## 🗃️ Database Schema

**Table:** `ds_salaries`

| Column | Type | Description |
|---|---|---|
| `work_year` | INT | Year the salary was paid |
| `experience_level` | VARCHAR(2) | EN / MI / SE / EX |
| `employment_type` | VARCHAR(2) | FT / PT / CT / FL |
| `job_title` | VARCHAR(100) | Role title |
| `salary` | NUMERIC | Original salary |
| `salary_currency` | VARCHAR(3) | ISO currency code |
| `salary_in_usd` | NUMERIC | Normalized USD value |
| `employee_residence` | VARCHAR(2) | ISO country code |
| `remote_ratio` | INT | 0 / 50 / 100 |
| `company_location` | VARCHAR(2) | ISO country code |
| `company_size` | VARCHAR(1) | S / M / L |

Relationships: single fact table; categorical columns act as implicit dimensions. Could be normalized into `dim_country`, `dim_role`, `dim_experience` for warehouse use.

---

## 🧪 Testing

### Unit Testing
```bash
pytest tests/
```

### Integration Testing
Validates the cleaning pipeline end-to-end against a fixture CSV and compares row counts, schema, and key aggregates.

### End-to-End Testing
Streamlit smoke test using `streamlit run --headless` and a Playwright script to assert KPI cards render.

**Tools:** `pytest`, `pandas.testing`, `Playwright`, `nbval` (notebook validation).

---

## ⚡ Performance Optimizations

- **`@st.cache_data`** on dataset loads — near-instant re-renders
- **Lazy loading** of raw data table (only when toggled)
- **Pagination** on heavy tables via Streamlit's native paging
- **Query optimization** — pre-aggregated DataFrames before plotting
- **Code splitting** — notebooks separated by stage (cleaning / EDA / viz)
- **Compression** — CSV outputs gzip-compatible for storage

---

## 🛡️ Security Features

- 🔐 **Authentication-ready** scaffolding (JWT secret in env)
- 🔐 **Authorization** stub for future admin dashboard
- 🔐 **No hard-coded credentials** anywhere in source
- 🔐 **Input validation** on all sidebar filters
- 🔐 **Rate limiting** ready via Streamlit / reverse proxy
- 🔐 **CSRF protection** when fronted by Nginx/Cloudflare
- 🔐 **Secure SQL practices** — parameterized queries only
- 🔐 **Read-only DB role** recommended for the app layer

---

## ☁️ Deployment

### Streamlit Community Cloud (recommended)
1. Push the repo to GitHub.
2. Connect at [share.streamlit.io](https://share.streamlit.io).
3. Set entrypoint: `Data-Analytics-Project/Python/Dashboard.py`.
4. Add secrets from `.env`.

### Render / Railway
- Use a `Procfile`: `web: streamlit run Python/Dashboard.py --server.port=$PORT --server.address=0.0.0.0`

### AWS / Azure
- Deploy via Docker on EC2 / App Service; serve behind Nginx with HTTPS.

### CI/CD
- **GitHub Actions** runs lint (`flake8`), format check (`black --check`), and notebook validation (`nbval`) on every PR.

---

## 🧩 Challenges & Solutions

- **Multi-currency salaries** — Salaries arrived in 10+ currencies. Solved by standardizing on `salary_in_usd` using historical FX rates and dropping the unreliable native columns from analysis.
- **Inconsistent job titles** — 50+ near-duplicate titles ("ML Engineer", "Machine Learning Engineer"). Built a normalization map in the cleaning script.
- **Outlier salaries** — A handful of $600K+ entries skewed averages. Used IQR-based winsorization in EDA while preserving raw values in the dashboard.
- **Streamlit re-render cost** — Initial reloads were slow. Resolved with `@st.cache_data` and pre-aggregation before plotting.
- **SQL portability** — Queries needed to work on both MySQL and PostgreSQL. Avoided dialect-specific functions; documented exceptions inline.

---

## 🔭 Future Improvements

1. Add **authentication** and per-user saved filters.
2. Integrate a **live FX rate API** for real-time currency normalization.
3. Build an **ML model** that predicts salary given role, country, and experience.
4. Add **role similarity clustering** (k-means on title embeddings).
5. Provide a **REST API** layer (FastAPI) over the cleaned dataset.
6. Add **scheduled email reports** of weekly market shifts.
7. Implement **dark mode** and accessibility (WCAG 2.1 AA).
8. Add **map-based geo visualization** with country-level choropleth.
9. Build a **comparison mode** (compare two filtered slices side-by-side).
10. Containerize with **Docker Compose** (app + Postgres + Adminer).
11. Add **multi-year forecasting** with Prophet / ARIMA.
12. Provide **PDF export** of dashboard snapshots.

---

## 🤝 Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feat/your-feature`.
3. Commit changes: `git commit -m "feat: add your feature"`.
4. Push: `git push origin feat/your-feature`.
5. Open a Pull Request.

**Coding standards**
- Format with `black`, lint with `flake8`.
- Conventional Commits (`feat:`, `fix:`, `docs:`, `refactor:`).
- Add/update tests for any new logic.
- Keep notebooks clean — clear outputs before committing.

---

## ❓ FAQ

**Q: Do I need a database to run the dashboard?**
A: No. The Streamlit app reads directly from `Cleaned_Data.csv`. SQL is optional.

**Q: Where is the dataset from?**
A: A public Data Science salaries dataset, cleaned and normalized inside this project.

**Q: Can I use this for my own region's data?**
A: Yes — replace `Raw_Data.csv` with your file and re-run `Data_Cleaning_Script.py`.

**Q: Why Streamlit instead of React?**
A: Streamlit lets analysts ship interactive apps without frontend overhead — ideal for analytics portfolios.

**Q: Is this production-ready?**
A: It's portfolio- and demo-ready. Add auth, monitoring, and a managed DB for production.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

# Author

**HARI BABU C H**

- **Role:** Frontend Developer | Data Analyst
- **GitHub:** [github.com/haribabux7](https://github.com/haribabux7)
- **LinkedIn:** [linkedin.com/in/haribabux7](https://www.linkedin.com/in/haribabux7)
- **Portfolio:** [haribabu.me](https://www.haribabu.me)
- **Email:** [haribabuc458@gmail.com](mailto:haribabuc458@gmail.com)

---

## 🙏 Acknowledgements

- **Open Source Libraries** — Pandas, NumPy, Plotly, Streamlit, Seaborn, Matplotlib
- **Community Datasets** — Public Data Science salary survey contributors
- **Learning Resources** — Streamlit Docs, Mode SQL Tutorial, Kaggle community notebooks
- **Inspiration** — levels.fyi, Stack Overflow Developer Survey, Glassdoor compensation reports

---

## 📌 Project Information

| Field | Value |
|---|---|
| Version | 1.0.0 |
| Designed Date | November 2025 |
