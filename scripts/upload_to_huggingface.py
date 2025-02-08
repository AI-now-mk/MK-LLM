
# Upload trained model to Hugging Face Model Hub

from huggingface_hub import HfApi, login

HF_TOKEN = "your_huggingface_token_here"  # Replace with your Hugging Face token
MODEL_PATH = "./models/mistral-finetuned-mk"
REPO_NAME = "AI-now-mk/MK-LLM-Mistral"

def upload_model():
    login(token=HF_TOKEN)
    api = HfApi()
    api.create_repo(REPO_NAME, exist_ok=True)
    api.upload_folder(folder_path=MODEL_PATH, repo_id=REPO_NAME, repo_type="model")
    print(f"✅ Model uploaded to Hugging Face: https://huggingface.co/{REPO_NAME}")

if __name__ == "__main__":
    upload_model()
