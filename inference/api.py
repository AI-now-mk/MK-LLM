
# Deploy fine-tuned model as an API
from fastapi import FastAPI
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_PATH = "./models/mistral-finetuned-mk"
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

app = FastAPI()

@app.get("/generate/")
def generate(prompt: str):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    return {"response": tokenizer.decode(outputs[0])}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
