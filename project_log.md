# 🧾 Project Log – US Accidents Risk

Day-1

## ✅ Tasks Completed

- [x] Created private GitHub repo `us-accidents-risk`
- [x] Added `.gitignore`, `README.md`, initial structure (`data/.gitkeep`, `notebooks/.gitkeep`, `scripts/download_data.py`, `requirements.txt`)
- [x] Updated `.gitignore` to exclude data folder but keep `.gitkeep`.
      Added these lines in the end of .gitignore file:
# Ignore dataset files
/data/*
!data/.gitkeep
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

`mkdir -p ~/.kaggle
mv ~/Desktop/Data_science+AI/us-accidents-risk/kaggle.json ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json`

✅ This sets the correct permissions and location for the Kaggle API to authenticate.

✅ Dataset Download
Wrote `scripts/download_data.py` with a `download_and_extract()`  function

Ran the script from terminal:

`cd ~/Desktop/Data_science+AI/us-accidents-risk
python3 scripts/download_data.py`

Downloaded and extracted the dataset to:

`/Users/deb/Desktop/Data_science+AI/us-accidents-risk/data/US_Accidents.csv`
File size: ~3GB unzipped

## 🚧 Next Steps
- [ ] Create initial EDA notebook and save to `notebooks/`
- [ ] Compute risk metrics by state, severity, and weather condition
- [ ] Create visualizations using seaborn or plotly
- [ ] Write final README with instructions
- [ ] Add collaborators and notify by June 11

