
# 🚀 Getting Started with MK-LLM

## 📥 Data Preparation
1️⃣ **Download Macedonian Wikipedia**  
```bash
python data/download_wikipedia.py
```

2️⃣ **Clean and Extract Text**  
```bash
python data/clean_wikipedia.py
```

3️⃣ **Tokenize the Text**  
```bash
python data/tokenize_text.py
```

## 🤖 Model Training
Fine-tune the Mistral 7B model:
```bash
python training/fine_tune_mistral.py
```
