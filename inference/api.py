
# FastAPI inference server with quantized model support

from fastapi import FastAPI
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_PATH = "./models/mistral-finetuned-mk"

app = FastAPI()

print("⏳ Loading model...")
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, torch_dtype=torch.float16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
print("✅ Model loaded successfully!")

@app.get("/generate/")
def generate(prompt: str, max_length: int = 100):
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=max_length)
    return {"response": tokenizer.decode(outputs[0], skip_special_tokens=True)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
