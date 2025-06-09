# 🧾 Project Log – US Accidents Risk

## Day 1

## ✅ Tasks Completed

- [x] Created private GitHub repo `us-accidents-risk`
- [x] Added `.gitignore`, `README.md`, initial structure (`data/.gitkeep`, `notebooks/.gitkeep`, `scripts/download_data.py`, `requirements.txt`)
- [x] Updated `.gitignore` to exclude data folder but keep `.gitkeep`.
      Added these lines in the end of .gitignore file:
 ```     
# Ignore dataset files
/data/*
!data/.gitkeep
```
- [x] Decided to use Google Colab for analysis (due to convenience and no setup)
- [x] Plan to use DuckDB for out-of-core querying of full dataset


### ✅ Setup

- Created private GitHub repository: `us-accidents-risk`
- Added folders: `/data/`, `/scripts/`, `/notebooks/`
- Added `.gitignore` to exclude data files but preserve folder structure using `.gitkeep`

---

### ✅ Kaggle API Setup

- Logged in to [https://www.kaggle.com/account](https://www.kaggle.com/account)
- Clicked "Create New API Token"
- Saved the downloaded `kaggle.json` file to my local project folder:

`/Users/deb/Desktop/Data_science+AI/us-accidents-risk/kaggle.json`


Then moved it to the secure hidden folder using:

```
mkdir -p ~/.kaggle
mv ~/Desktop/Data_science+AI/us-accidents-risk/kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
```

✅ This sets the correct permissions and location for the Kaggle API to authenticate.

### ✅ Dataset Download
Wrote `scripts/download_data.py` with a `download_and_extract()`  function

Ran the script from terminal:

```
cd ~/Desktop/Data_science+AI/us-accidents-risk
python3 scripts/download_data.py
```

Downloaded and extracted the dataset to:

`/Users/deb/Desktop/Data_science+AI/us-accidents-risk/data/US_Accidents.csv`

File size: ~3GB unzipped

### ✅ Dataset Download Script Committed

- Created and saved `scripts/download_data.py` inside the repository
- This script authenticates with the Kaggle API using `kaggle.json` and downloads the **US Accidents** dataset to the local `data/` directory.
- Committed directly to the `main` branch with the message:

  ```
  Add dataset download script using Kaggle API.  This script authenticates using kaggle.json and downloads the US Accidents dataset to the data/ folder.```

### ✅ GitHub Access from Terminal Setup

- Installed [GitHub CLI (`gh`)](https://cli.github.com/) using Homebrew:
  ```bash
  brew install gh ```

  Authenticated GitHub from terminal:

`gh auth login`

→ Logged in using web browser authentication.
→ Confirmed successful login with:

`gh auth status`

Removed manually created local project folder and re-cloned the GitHub repository to link it properly:

```
cd ~/Desktop/Data_science+AI
mv us-accidents-risk mv us-accidents-risk-1 # renamed previously existing directory
git clone https://github.com/drtirnadeb/us-accidents-risk.git
cd us-accidents-risk
```
✅ Now working entirely from a Git-tracked folder connected to GitHub for terminal-based commits, branching, and pull requests.


### ✅ Added Exploratory Data Analysis (EDA) Notebook – DuckDB

Created us_accidents_duckdb_eda.ipynb under notebooks/

The notebook performs initial analysis using DuckDB, covering column summaries, missing values, state-wise accident distribution, and basic descriptive statistics

This file is available in the eda-duckdb feature branch and has been submitted via pull request for review.


### ✅ GitHub Workflow Steps


```
# 1. Created GitHub issue to track EDA task
# (On GitHub) → Issues → New → Title: "Initial EDA with DuckDB"

# 2. Created and switched to a new branch
git checkout -b eda-duckdb

# 3. Saved notebook to the notebooks/ folder inside the cloned repo

# 4. Staged the new notebook
git add notebooks/us_accidents_duckdb_eda.ipynb

# 5. Committed the notebook with a descriptive message
git commit -m "Add initial DuckDB-based EDA on US Accidents dataset"

# 6. Pushed the feature branch to GitHub
git push origin eda-duckdb

# 7. Opened a pull request on GitHub from eda-duckdb → main
#     → Title: Initial EDA with DuckDB
#     → Description: Summary of what's inside the notebook
#     → Linked it to the GitHub issue (e.g., Closes #1)

```


## 🚧 Next Steps
- [ ] Create initial EDA notebook and save to `notebooks/`
- [ ] Compute risk metrics by state, severity, and weather condition
- [ ] Create visualizations using seaborn or plotly
- [ ] Write final README with instructions
- [ ] Add collaborators and notify by June 9

 ---

## Day 2

## ✅ Tasks Completed

- Performed **full-scale Exploratory Data Analysis (EDA)** on the complete US Accidents dataset (~3GB), including:
  - Initial correlation heatmap and pairplot on subset
  - Followed by complete temporal, geographical, and severity-based analysis using the full dataset

- Answered all **three assigned questions** from the prompt:
  1. Accident trends over time (yearly, seasonal, monthly, weekly, hourly)
  2. Severity trends over time and across geography
  3. Most common weather conditions by state

- Created relevant plots and saved all outputs into `plots/` (e.g., `plots/time`, `plots/correlation`, `plots/weather`)  
  Final Jupyter notebook updated in: `notebooks/us_accidents_duckdb_eda.ipynb`

- Created a **feature branch** to track this major addition:
  `git checkout -b feature/full-eda-assignment`

Committed notebook and image files, pushed to GitHub:

   ```
git add notebooks/us_accidents_duckdb_eda.ipynb
git add plots/
git commit -m "Add full EDA notebook and generated plots for full assignment"
git push origin feature/full-eda-assignment
```


* Opened a pull request from `feature/full-eda-assignment → main` with description:

This PR includes the completed Exploratory Data Analysis (EDA) assignment:

- Accident trends by year, season, month, weekday, and hour
- Severity trends over time and across geography
- Correlation heatmap and pairplot of key numerical features
- Most common weather conditions by state
- US-wide accident density and severity mapping
- All plots saved under `plots/` and final notebook in `notebooks/`
- README and project log updated

* Successfully **merged the pull request** into main and deleted the feature branch for cleanup

* Also created a **GitHub Issue** to formally track this assignment task:

```Title: Complete EDA Assignment (Full Dataset)
Description: Includes all visualizations, questions answered, and final project notebook
Labels: enhancement, assignment
```


### 📝 Purpose of Workflow

- Followed a **basic Gitflow strategy** as outlined in the assignment:
  - Opened an **issue** and a **corresponding feature branch** (`feature/full-eda-assignment`) to isolate work on the EDA assignment
  - Used a **pull request** to review and merge changes into `main` once complete
  - Maintained a `.gitignore` file that excludes large data files (`/data/*`) and any virtual environments

- This strategy supports **continuous delivery**, clean version control, and allows for **transparent code review and discussion** before merging.
- Ensures that all major contributions (e.g., EDA notebook and visualizations) are **modular, well-documented, and traceable** within the GitHub repository.


---

## Day 3–4: Risk Metric Computation and Visualization

### ✅ Tasks Completed

- Computed **state-level accident risk metrics** based on the full US Accidents dataset:
  - Grouped accident records by state
  - Calculated:
    - Total accident count
    - Average severity score (scale 1–4)
    - Population-adjusted accident rate (per 100,000 people)
    - Composite risk score using a weighted average of normalized severity and rate

- Created **multiple choropleth maps** to visualize:
  - 📍 Accident Rate per 100,000 people (`accident_rate_per_100k.png`)
  - ⚠️ Average Severity by state (`avg_severity_by_state.png`)
  - 🧩 Composite Risk Score (`composite_risk_map.png`)

- Added **barplots and heatmaps** for deeper breakdowns:
  - By severity level and year
  - By time of day, daylight vs. darkness
  - By top 5 weather conditions (normalized)

- Saved all metrics and figures under structured folders inside `notebooks/outputs/`:
  - `outputs/metrics/`
  - `outputs/risk_metrics/`
  - `outputs/3_states/`

- Exported final **state-level risk scores** as a CSV file:
  - `notebooks/state_risk_scores.csv`

---

### 🔧 Git Workflow

- Created new feature branch for this module:
`git checkout -b feature/risk-metrics`

- Committed the notebook and relevant assets:

```
git add notebooks/us_accidents_risk_metrics.ipynb README.md
git add notebooks/outputs/ metrics/ plots/
git commit -m "Add risk metric analysis notebook and update README"
git push origin feature/risk-metrics
```


- Opened a pull request from `feature/risk-metrics → main`:
- Described the metrics computed and linked visualizations
- Successfully merged the PR and deleted the branch after merge

---

### 📌 GitHub Issue Tracking

- Created a new **GitHub Issue** to track this milestone:
```
Title: Add Risk Metric Computation and Visual Analysis for US Accidents Dataset
Description: Includes all computed metrics, choropleth visualizations, and temporal/weather breakdowns
Labels: enhancement, data-analysis
```

* Closed the issue after successful PR merge

 ### 📝 Notes
 
Used `folium` for interactive mapping; exported static versions as `.png` for reproducibility in notebook and README

Updated `README.md` to include a section: `📊 Risk Metric` Computation with notebook link and description

Maintained modularity and clean organization under `notebooks/, outputs/, and plots/`

---


## Day 5 – Packaging the RiskAnalyzer Module and Final Enhancements

### 🧩 Key Tasks Completed

- ✅ Factored the `RiskAnalyzer` class to support **CSV-based input** via `data_path` in addition to direct `DataFrame` input.
- ✅ Modularized the code as a **Python package** named `accidents` and added an `__init__.py` file to enable imports.
- ✅ Created a minimal working example script: `examples/example_usage.py` demonstrating basic usage.
- ✅ Created a sample CSV file (`data/sample_accidents.csv`) for testing the new feature.
- ✅ Installed the package locally using `pip install -e .` and validated both direct and CSV input methods.
- ✅ Opened a new **feature branch** (`feature/package-risk-analyzer`) and merged it via a pull request into `main`.

### 📦 Benefits
- Package is now reusable across notebooks and projects.
- Clean structure supports both programmatic use (`from accidents import RiskAnalyzer`) and CLI-style loading.
- Simplifies future unit testing, CI integration, and documentation.








