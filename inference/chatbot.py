
# Simple chatbot using the fine-tuned Macedonian LLM

from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_PATH = "./models/mistral-finetuned-mk"

def load_model():
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    return model, tokenizer

def chat():
    model, tokenizer = load_model()
    print("🤖 MK-LLM Chatbot is ready! Type 'exit' to quit.")
    while True:
        prompt = input("You: ")
        if prompt.lower() == "exit":
            break
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(**inputs)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chat()
