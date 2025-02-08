
# 🇲🇰 MK-LLM: Open Macedonian Language Model

## 🌍 About This Project
MK-LLM is **Macedonia's first open-source Large Language Model (LLM)**, built for and by the community.  
This project is led by **AI Now - Association for Artificial Intelligence in Macedonia**.  

📌 **Website:** [www.ainow.mk](https://www.ainow.mk)  
📩 **Contact:** [contact@ainow.mk](mailto:contact@ainow.mk)  
🔹 **Hugging Face Model Repo:** Coming Soon  

## 📂 Repository Overview
- `data/` → Scripts for **data collection, cleaning, and tokenization**.
- `training/` → Scripts for **fine-tuning the model** (Multi-GPU supported!).
- `models/` → Directory for **storing trained models**.
- `inference/` → Scripts to **deploy the trained model as an API** (FastAPI-based).
- `notebooks/` → Jupyter notebooks for research & evaluation.
- `scripts/` → Utility scripts (Hugging Face model upload, dataset processing).
- `docs/` → Documentation for contributors & guidelines.

## 🚀 How to Get Started
```bash
git clone https://github.com/AI-now-mk/MK-LLM.git
cd MK-LLM
pip install -r requirements.txt
```

## 🏋️‍♂️ Fine-Tune the Model (Multi-GPU Supported)
```bash
python training/train_pipeline.py
```

## 🌐 Deploy the API for Inference
```bash
uvicorn inference.api:app --host 0.0.0.0 --port 8000
```

## 📤 Upload Model to Hugging Face
1. Add your Hugging Face token inside `scripts/upload_to_huggingface.py`
2. Run the script:
```bash
python scripts/upload_to_huggingface.py
```

## 🤝 How to Contribute
See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for details. Also, check [`docs/GITHUB_ISSUES.md`](./docs/GITHUB_ISSUES.md) for open-source tasks!

🚀 **Join AI Now in making AI accessible to Macedonia!** 🇲🇰
