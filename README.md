# 🇲🇰 MK-LLM: The First Open Macedonian Language Model

## 🌍 About This Project
MK-LLM is Macedonia's first open-source Large Language Model (LLM), developed for the community, by the community. This project is led by AI Now - Association for Artificial Intelligence in Macedonia.

📌 **Website:** [www.ainow.mk](https://www.ainow.mk)  
📩 **Contact:** [contact@ainow.mk](mailto:contact@ainow.mk)  
🛠 **Model:** [MK-LLM-Mistral](https://huggingface.co/ainowmk/MK-LLM-Mistral)  
💻 **GitHub:** [MK-LLM](https://github.com/AI-now-mk/MK-LLM)

## 🆕 Latest Updates (2024-01-09)
- Implemented Mistral-7B training pipeline
- Added comprehensive data collection system
- Integrated Wikipedia and public data sources
- Optimized for Macedonian language
- Added testing and validation tools

## 📂 Repository Structure
```plaintext
MK-LLM/
├── data/
│   ├── wikipedia/          # Wikipedia data processing
│   └── process_all_data.py # Multi-source data collection
├── examples/
│   ├── train_mistral_mk.py # Training script
│   ├── data_loader.py      # Data utilities
│   └── test_local.py       # Testing tools
└── models/                 # Trained models
```

## 🚀 Getting Started
1. Clone the repository:
```bash
git clone https://github.com/AI-now-mk/MK-LLM.git
cd MK-LLM
```
pip install -r requirements.txt
