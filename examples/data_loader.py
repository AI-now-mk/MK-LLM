from datasets import Dataset, load_dataset
import pandas as pd
import os

def load_mk_dataset():
    """Load and prepare Macedonian dataset for training"""
    data_sources = {
        'wikipedia': 'data/cleaned/mk_wiki.txt',
        'news': 'data/cleaned/mk_news.txt',
        'books': 'data/cleaned/mk_books.txt',
        'web': 'data/cleaned/mk_web.txt'
    }
    
    texts = []
    for source, path in data_sources.items():
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                texts.extend(f.readlines())
    
    # Create dataset
    dataset = Dataset.from_dict({
        'text': texts
    })
    
    return dataset