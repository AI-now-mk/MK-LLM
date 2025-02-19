import requests
import bz2
import os
from tqdm import tqdm

WIKI_URL = "https://dumps.wikimedia.org/mkwiki/latest/mkwiki-latest-pages-articles.xml.bz2"
OUTPUT_DIR = "data/wikipedia/raw"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "mk_wiki.xml")

def download_wiki_dump():
    # Create directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    print(f"Downloading Macedonian Wikipedia dump...")
    response = requests.get(WIKI_URL, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    # Download the compressed file
    with open(OUTPUT_FILE + '.bz2', 'wb') as f:
        with tqdm(total=total_size, unit='iB', unit_scale=True) as pbar:
            for data in response.iter_content(1024):
                f.write(data)
                pbar.update(len(data))
    
    print("Extracting bz2 file...")
    with bz2.open(OUTPUT_FILE + '.bz2', 'rb') as source:
        with open(OUTPUT_FILE, 'wb') as dest:
            dest.write(source.read())
            
    print(f"Wikipedia dump downloaded and extracted to {OUTPUT_FILE}")

if __name__ == "__main__":
    download_wiki_dump()