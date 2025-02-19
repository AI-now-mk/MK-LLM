import xml.etree.ElementTree as ET
import re
from tqdm import tqdm
import os

INPUT_FILE = "data/wikipedia/raw/mk_wiki.xml"
OUTPUT_FILE = "data/wikipedia/processed/mk_wiki_text.txt"

def clean_wiki_text(text):
    # Remove wiki markup
    text = re.sub(r'\{\{[^\}]*\}\}', '', text)  # Remove templates
    text = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]', r'\1', text)  # Clean links
    text = re.sub(r'==+.*?==+', '', text)  # Remove headers
    text = re.sub(r'<ref[^>]*>.*?</ref>', '', text)  # Remove references
    text = re.sub(r'<!--.*?-->', '', text)  # Remove comments
    text = re.sub(r'\s+', ' ', text)  # Clean whitespace
    return text.strip()

def create_directories():
    output_dir = os.path.dirname(OUTPUT_FILE)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def parse_wiki_dump():
    create_directories()
    
    context = ET.iterparse(INPUT_FILE, events=('end',))
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        for event, elem in tqdm(context):
            if elem.tag.endswith('text'):
                text = elem.text
                if text and len(text) > 100:
                    cleaned_text = clean_wiki_text(text)
                    if cleaned_text:
                        f.write(cleaned_text + '\n\n')
            elem.clear()

if __name__ == "__main__":
    parse_wiki_dump()