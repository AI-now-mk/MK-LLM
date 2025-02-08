
# Script to preprocess additional text datasets

import os

RAW_DATA_DIR = "data/raw"
PROCESSED_DATA_DIR = "data/processed"

def preprocess_files():
    for filename in os.listdir(RAW_DATA_DIR):
        raw_file_path = os.path.join(RAW_DATA_DIR, filename)
        processed_file_path = os.path.join(PROCESSED_DATA_DIR, filename)
        with open(raw_file_path, "r", encoding="utf-8") as rf, open(processed_file_path, "w", encoding="utf-8") as pf:
            for line in rf:
                pf.write(line.strip() + "\n")
    print("✅ Data preprocessing complete!")

if __name__ == "__main__":
    preprocess_files()
