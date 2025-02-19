import os
import json
from langdetect import detect
from collections import defaultdict

def test_collected_data():
    print("Testing collected Macedonian data...")
    
    # Paths
    raw_data = os.path.join("data", "raw", "mk_web_data.json")
    cleaned_data = os.path.join("data", "cleaned", "mk_combined_data.txt")
    
    # Test raw data
    if os.path.exists(raw_data):
        with open(raw_data, 'r', encoding='utf-8') as f:
            web_data = json.load(f)
            
        # Analyze sources
        sources = defaultdict(int)
        categories = defaultdict(int)
        total_chars = 0
        
        for item in web_data:
            sources[item['source']] += 1
            categories[item['category']] += 1
            total_chars += len(item['text'])
        
        print("\n📊 Raw Data Statistics:")
        print(f"Total entries: {len(web_data)}")
        print(f"Total characters: {total_chars:,}")
        print(f"Average entry length: {total_chars/len(web_data):,.0f} characters")
        
        print("\n📑 Categories:")
        for cat, count in categories.items():
            print(f"- {cat}: {count} entries")
    
    # Test cleaned data
    if os.path.exists(cleaned_data):
        with open(cleaned_data, 'r', encoding='utf-8') as f:
            cleaned_texts = f.read().split('\n\n')
        
        mk_count = 0
        total_len = 0
        
        print("\n🧹 Cleaned Data Statistics:")
        print(f"Total entries: {len(cleaned_texts)}")
        
        # Test random samples
        print("\n📝 Testing random samples:")
        import random
        for i, text in enumerate(random.sample(cleaned_texts, min(5, len(cleaned_texts)))):
            try:
                is_mk = detect(text) == 'mk'
                mk_count += 1 if is_mk else 0
                total_len += len(text)
                print(f"\nSample {i+1} ({len(text)} chars):")
                print(f"First 100 chars: {text[:100]}...")
                print(f"Language detected: {'Macedonian ✅' if is_mk else 'Other ❌'}")
            except:
                continue
        
        print(f"\nAverage text length: {total_len/len(cleaned_texts):,.0f} characters")

if __name__ == "__main__":
    test_collected_data()