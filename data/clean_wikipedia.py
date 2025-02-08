
# Script to clean and preprocess Macedonian Wikipedia text

import re

def clean_text(text):
    text = re.sub(r'\[.*?\]', '', text)  # Remove Wikipedia category links
    text = re.sub(r'\{\{.*?\}\}', '', text)  # Remove Wikipedia templates
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = text.replace("\n", " ").strip()
    return text

if __name__ == "__main__":
    print("Data cleaning script ready to process text!")
