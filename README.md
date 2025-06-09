# 🚗 US Accidents Risk Analysis (2016–2023)

This project analyzes traffic accident patterns in the United States using a large-scale Kaggle dataset. The goal is to explore public health risk factors through state-level trends, severity breakdowns, and weather conditions.

## 🔍 Dataset
- Source: [Kaggle – US Accidents (2016–2023)](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)
- Contains 7.7 million records from 49 US states

## 📁 Project Structure
- `data/`: Downloaded dataset (ignored by Git)
- `scripts/`: Data download and processing scripts
- `notebooks/`: Exploratory notebooks and visualizations

  <pre lang="md"> ## 📁 Project Structure <details> <summary><strong>📂 Repository Layout (click to expand)</strong></summary> ``` us-accidents-risk/ │ ├── accidents/ # Python package with RiskAnalyzer class │ ├── __init__.py │ └── risk_analyzer.py │ ├── data/ # Dataset folder (ignored by Git) │ ├── docs/ # Public HTML for GitHub Pages │ └── us_composite_risk_map.html │ ├── examples/ # Standalone usage scripts │ └── example_usage.py │ ├── notebooks/ # All analysis and visualization notebooks │ ├── us_accidents_duckdb_eda.ipynb │ ├── us_accidents_risk_metrics.ipynb │ ├── test_risk_analyzer.ipynb │ ├── test_risk_analyzer_package.ipynb │ ├── plots/ # Generated figures │ ├── outputs/ # CSVs, maps, exports │ └── composite_risk_map.png # Screenshot for README │ ├── scripts/ # Data download and setup scripts │ └── download_data.py │ ├── README.md ├── project_log.md # Running notes on project progress ├── requirements.txt ├── setup.py └── pyproject.toml ``` </details> </pre>

## 🛠 Tech Stack
- Python, DuckDB, Pandas, Seaborn/Matplotlib
- Google Colab for analysis

## 🚀 How to Use
1. Add your `kaggle.json` file in Colab
2. Run `scripts/download_data.py` to fetch the dataset
3. Analyze and visualize data in `notebooks/`

## 📦 Dependencies

- Python 3.9+
- pandas
- seaborn / matplotlib
- duckdb
- kaggle

Install all dependencies with:

`pip install -r requirements.txt`

## 📌 To Do
- [x] GitHub setup
- [x] Dataset download
- [x] EDA & visualizations
- [x] Final writeup
- [x] Compute risk metrics


## 🛠 Local Setup Notes (for reproducibility)

To download the dataset locally:

1. Generate your Kaggle API token at [kaggle.com/account](https://www.kaggle.com/account)
2. Save `kaggle.json` to the hidden folder:

```bash
mkdir -p ~/.kaggle
mv /path/to/kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
```
Run the download script:

`python scripts/download_data.py`


## 📊 Exploratory Data Analysis (EDA)

An initial exploratory data analysis has been conducted using [DuckDB](https://duckdb.org/), enabling fast SQL queries on the full dataset without loading it entirely into memory.

📁 Notebook: [`notebooks/us_accidents_duckdb_eda.ipynb`](notebooks/us_accidents_duckdb_eda.ipynb)

Key insights covered:
- Column types and dataset schema
- Missing value overview across features
- Severity distribution statistics
- Top 10 accident-prone U.S. states

This analysis serves as a foundation for computing risk metrics and identifying high-impact variables.

### A complete EDA assignment has been completed, including:

- Accident trends over **year, season, month, weekday, and hour**
- Severity distribution across **time and geography**
- Most common **weather conditions** by state
- US-wide **accident density and severity heatmaps**

📁 See final notebook: [`notebooks/us_accidents_duckdb_eda.ipynb`](notebooks/us_accidents_duckdb_eda.ipynb)  
📁 Generated plots saved under: [`notebooks/plots/`](notebooks/plots/)


➡️ See the related [pull request](https://github.com/drtirnadeb/us-accidents-risk/pull/1) for full implementation details. 
➡️ See the related [pull request](https://github.com/drtirnadeb/us-accidents-risk/pull/2) for full implementation details of the full EDA assignment.


## 📊 Risk Metric Computation

We performed an in-depth risk analysis of U.S. traffic accidents using the [US Accidents Dataset (2021)](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents).

### ✔️ Overview of Analysis

- Cleaned and filtered the dataset for valid geolocation and severity data
- Computed state-level metrics:
  - **Total accident count**
  - **Average severity**
  - **Accident rate normalized by population**
  - **Composite risk score** combining rate and severity
- Stratified plots by:
  - **Top 5 weather conditions** (e.g., Clear, Rain, Haze, Snow, Fog)
  - **Time of day** and **daylight condition** (e.g., Night vs. Day)
- Visualizations include heatmaps, bar charts, and choropleth maps

➡️ See `notebooks/us_accidents_risk_metrics.ipynb` for all plots and detailed breakdowns.


---

## 📦 RiskAnalyzer Python Package

This project includes a reusable Python package: `accidents`, containing a modular class for risk metric computation and visualization.

### 🔧 Installation

Clone the repository and install the package in editable mode:

```
git clone https://github.com/drtirnadeb/us-accidents-risk.git
cd us-accidents-risk
pip install -e
```

### 🚀 Example Usage

You can use the `RiskAnalyzer` class directly in your scripts:

```
from accidents import RiskAnalyzer

### Option 1: Load from CSV
analyzer = RiskAnalyzer(
    data_path='data/sample_accidents.csv',
    population_dict={
        'CA': 39538223, 'TX': 29145505, 'NY': 20201249
    }
)

### Option 2: Load from DataFrame
### analyzer = RiskAnalyzer(df=my_dataframe, population_dict=...)

### Compute metrics
risk_df = analyzer.compute_risk_scores()
analyzer.plot_risk_map()
analyzer.plot_time_analysis()
analyzer.plot_weather_analysis()
```

### 📁 Additional Files

* 📄 `accidents/risk_analyzer.py`: Source code for the reusable class

* 🧪 `notebooks/test_risk_analyzer.ipynb`: Full test with dummy data

* 💡 `examples/example_usage.py`: Standalone script to test package locally

![License](https://img.shields.io/badge/license-MIT-blue)
![Status](https://img.shields.io/badge/status-Complete-brightgreen)


