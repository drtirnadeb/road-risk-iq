# 🧾 Project Log – US Accidents Risk

Day-1

## ✅ Tasks Completed

- [x] Created private GitHub repo `us-accidents-risk`
- [x] Added `.gitignore`, `README.md`, initial structure (`data/.gitkeep`, `notebooks/.gitkeep`, `scripts/download_data.py`)
- [x] Updated `.gitignore` to exclude data folder but keep `.gitkeep`.
      Added these lines in the end of .gitignore file:
# Ignore dataset files
/data/*
!data/.gitkeep
- [x] Decided to use Google Colab for analysis (due to convenience and no setup)
- [x] Plan to use DuckDB for out-of-core querying of full dataset

## 🚧 Next Steps
- [ ] Upload `kaggle.json` in Colab and download dataset using script
- [ ] Create initial EDA notebook and save to `notebooks/`
- [ ] Compute risk metrics by state, severity, and weather condition
- [ ] Create visualizations using seaborn or plotly
- [ ] Write final README with instructions
- [ ] Add collaborators and notify by June 11

