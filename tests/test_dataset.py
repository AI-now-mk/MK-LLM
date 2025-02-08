
# Script to check dataset integrity

import os

PROCESSED_DATA_PATH = "data/processed/mk_wiki_clean.txt"

def check_dataset():
    if os.path.exists(PROCESSED_DATA_PATH):
        with open(PROCESSED_DATA_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
        print(f"✅ Dataset contains {len(lines)} lines.")
    else:
        print("❌ Processed dataset not found!")

if __name__ == "__main__":
    check_dataset()
