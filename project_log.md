# 🧾 Project Log – US Accidents Risk

Day-1

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

## 🚧 Next Steps
- [ ] Create initial EDA notebook and save to `notebooks/`
- [ ] Compute risk metrics by state, severity, and weather condition
- [ ] Create visualizations using seaborn or plotly
- [ ] Write final README with instructions
- [ ] Add collaborators and notify by June 11

