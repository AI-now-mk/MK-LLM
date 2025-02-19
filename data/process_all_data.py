import os
import json
from langdetect import detect
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm
import time

def collect_mk_websites_data():
    print("Collecting data from Macedonian websites...")
    start_time = time.time()
    
    # Define websites to scrape
    websites = {
        'news': [
            'https://time.mk',
            'https://daily.mk',
            'https://www.fakulteti.mk',
            'https://www.akademik.mk',
            'https://www.mkd.mk'
        ],
        'government': [
            'https://mon.gov.mk',
            'http://www.ujp.gov.mk',
            'https://fzo.org.mk',
            'https://uslugi.gov.mk',
            'https://vlada.mk',
            'https://www.sobranie.mk'
        ],
        'education': [
            'https://ukim.edu.mk',
            'https://www.finki.ukim.mk',
            'https://www.feit.ukim.edu.mk',
            'https://www.pmf.ukim.edu.mk'
        ],
        'culture': [
            'https://www.kultura.gov.mk',
            'https://mmc.mk',
            'https://www.mkc.mk'
        ],
        'business': [
            'https://www.mchamber.mk',
            'https://www.nbrm.mk',
            'https://www.stat.gov.mk'
        ],
        'tech': [
            'https://www.ainow.mk/mk',
            'https://it.mk',
            'https://gsix.mk'
        ]
    }
    
    collected_texts = []
    total_sites = sum(len(urls) for urls in websites.values())
    
    with tqdm(total=total_sites, desc="Processing websites") as pbar:
        for category, urls in websites.items():
            print(f"\nProcessing {category} websites...")
            for url in urls:
                try:
                    response = requests.get(url, timeout=10, verify=False)
                    response.encoding = 'utf-8'
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    # Find all text content
                    content = soup.find_all([
                        'p', 'article', 'section',
                        'div.content', 'div.entry-content',
                        'div.post-content', 'div.article-body',
                        '.mk-content'  # Common class for Macedonian content
                    ])
                    
                    # Add specific content areas
                    main_content = soup.find_all(class_=['content-area', 'main-content', 'post-content'])
                    if main_content:
                        content.extend(main_content)
                        
                    # Add news article content
                    articles = soup.find_all(['article', 'div'], class_=['vest', 'article', 'news-item'])
                    if articles:
                        content.extend(articles)
                    for item in content:
                        text = item.get_text().strip()
                        if len(text) > 150:  # Longer text threshold
                            collected_texts.append({
                                'category': category,
                                'source': url,
                                'text': text
                            })
                    
                    # Also collect links and process them
                    links = soup.find_all('a', href=True)
                    for link in links[:5]:  # Process first 5 links from each site
                        full_url = urljoin(url, link['href'])
                        if url in full_url:  # Only internal links
                            try:
                                sub_response = requests.get(full_url, timeout=5, verify=False)
                                sub_response.encoding = 'utf-8'
                                sub_soup = BeautifulSoup(sub_response.text, 'html.parser')
                                sub_content = sub_soup.find_all(['p', 'article'])
                                
                                for item in sub_content:
                                    text = item.get_text().strip()
                                    if len(text) > 150:
                                        collected_texts.append({
                                            'category': category,
                                            'source': full_url,
                                            'text': text
                                        })
                            except:
                                continue
                                
                    pbar.update(1)
                    pbar.set_description(f"Processing {url[:30]}...")
                except Exception as e:
                    print(f"Error processing {url}: {e}")
                    pbar.update(1)
                    continue
    
    elapsed_time = time.time() - start_time
    print(f"\nTotal collection time: {elapsed_time/60:.2f} minutes")
    return collected_texts

def process_all_data():
    print("Processing all Macedonian data sources...")
    
    # Create directories
    raw_dir = os.path.join("data", "raw")
    wiki_dir = os.path.join("data", "wikipedia", "processed")
    output_dir = os.path.join("data", "cleaned")
    
    for directory in [raw_dir, output_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    # Collect new website data
    web_texts = collect_mk_websites_data()
    
    # Save raw web data
    web_file = os.path.join(raw_dir, "mk_web_data.json")
    with open(web_file, 'w', encoding='utf-8') as f:
        json.dump(web_texts, f, ensure_ascii=False, indent=2)
    
    all_texts = []
    
    # Add web texts
    all_texts.extend([item['text'] for item in web_texts])
    
    # Add Wikipedia data if exists
    wiki_file = os.path.join(wiki_dir, "mk_wiki_text.txt")
    if os.path.exists(wiki_file):
        with open(wiki_file, 'r', encoding='utf-8') as f:
            wiki_texts = f.readlines()
            all_texts.extend(wiki_texts)
    
    # Clean and validate
    cleaned_texts = []
    for text in all_texts:
        text = text.strip()
        if len(text) > 150:
            try:
                if detect(text) == 'mk':
                    cleaned_texts.append(text)
            except:
                continue
    
    # Save final dataset
    output_file = os.path.join(output_dir, "mk_combined_data.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(cleaned_texts))
    
    print(f"Successfully processed and saved {len(cleaned_texts)} text samples")

if __name__ == "__main__":
    process_all_data()