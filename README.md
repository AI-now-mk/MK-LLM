# 🇲🇰 MK-LLM: The First Open Macedonian Language Model  

## 🌍 About This Project  
MK-LLM is **Macedonia’s first open-source Large Language Model (LLM)**, developed for the community, by the community.  
This project is led by **AI Now - Association for Artificial Intelligence in Macedonia**, to create an AI system that understands and generates text in Macedonian.  

📌 **Website:** [www.ainow.mk](https://www.ainow.mk)  
📩 **Contact:** [contact@ainow.mk](mailto:contact@ainow.mk)  
🛠 **Hugging Face Model Repo:** [MK-LLM-Mistral](https://huggingface.co/ainowmk/MK-LLM-Mistral)  
💻 **GitHub Repository:** [MK-LLM](https://github.com/AI-now-mk/MK-LLM)  

---

## 📂 Repository Overview  
This repository contains everything needed to **build, train, and deploy the Macedonian LLM**.

- `data/` → Scripts for **data collection, cleaning, and tokenization**.
  - `raw/` → Unprocessed Macedonian text data.
  - `cleaned/` → Preprocessed and cleaned data.
  - `tokenized/` → Tokenized datasets ready for training.
- `training/` → Scripts for **fine-tuning the model** (Multi-GPU supported!).
  - `train.py` → Training script for fine-tuning.
  - `evaluate.py` → Evaluation script for performance testing.
- `models/` → Directory for **storing trained models**.
  - `mistral-finetuned-mk/` → Fine-tuned Macedonian Mistral model.
- `inference/` → Scripts to **deploy the trained model as an API** (FastAPI-based).
  - `api.py` → FastAPI script to serve the model.
- `notebooks/` → Jupyter notebooks for research & evaluation.
- `scripts/` → Utility scripts for data processing & Hugging Face uploads.
  - `download_wikipedia.py` → Scrapes and extracts Wikipedia articles in Macedonian.
  - `clean_data.py` → Cleans raw text data.
  - `tokenize_data.py` → Tokenizes the dataset for training.
  - `upload_to_huggingface.py` → Uploads model to Hugging Face.
- `docs/` → Documentation for contributors & guidelines.
- `README.md` → Documentation (this file).
- `requirements.txt` → Python dependencies.
- `.gitignore` → Ignored files.
- `LICENSE` → License (Apache 2.0).

---

## 🚀 How to Get Started  
To install dependencies and set up the project, run:
```bash
git clone https://github.com/AI-now-mk/MK-LLM.git
cd MK-LLM
pip install -r requirements.txt
