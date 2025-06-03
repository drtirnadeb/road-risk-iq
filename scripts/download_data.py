import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_and_extract(dataset="sobhanmoosavi/us-accidents", download_dir="data"):
    os.makedirs(download_dir, exist_ok=True)

    api = KaggleApi()
    api.authenticate()

    print("📥 Downloading dataset...")
    api.dataset_download_files(dataset, path=download_dir, unzip=True)
    print("✅ Dataset downloaded and extracted to:", download_dir)

if __name__ == "__main__":
    download_and_extract()
