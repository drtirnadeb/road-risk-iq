# 🚗 US Accidents Risk Analysis (2016–2023)

This project analyzes traffic accident patterns in the United States using a large-scale Kaggle dataset. The goal is to explore public health risk factors through state-level trends, severity breakdowns, and weather conditions.

## 🔍 Dataset
- Source: [Kaggle – US Accidents (2016–2023)](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)
- Contains 7.7 million records from 49 US states

## 📁 Project Structure
- `data/`: Downloaded dataset (ignored by Git)
- `scripts/`: Data download and processing scripts
- `notebooks/`: Exploratory notebooks and visualizations

## 🛠 Tech Stack
- Python, DuckDB, Pandas, Seaborn/Matplotlib
- Google Colab for analysis

## 🚀 How to Use
1. Add your `kaggle.json` file in Colab
2. Run `scripts/download_data.py` to fetch the dataset
3. Analyze and visualize data in `notebooks/`

## 📌 To Do
- [x] GitHub setup
- [x] Dataset download
- [ ] Compute risk metrics
- [ ] EDA & visualizations
- [ ] Final writeup

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

➡️ See the related [pull request](https://github.com/drtirnadeb/us-accidents-risk/pull/1) for full implementation details. 



---
