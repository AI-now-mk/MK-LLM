
# Script to download Macedonian Wikipedia dataset
import requests

WIKI_URL = "https://dumps.wikimedia.org/mkwiki/latest/mkwiki-latest-pages-articles.xml.bz2"
OUTPUT_FILE = "data/raw/mk_wiki.xml.bz2"

def download_wikipedia():
    print(f"Downloading Wikipedia dump from {WIKI_URL}...")
    response = requests.get(WIKI_URL, stream=True)
    with open(OUTPUT_FILE, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)
    print(f"Download complete: {OUTPUT_FILE}")

if __name__ == "__main__":
    download_wikipedia()
