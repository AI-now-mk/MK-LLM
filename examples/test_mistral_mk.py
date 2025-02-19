import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def load_and_test_model():
    # Load Mistral-7B model
    model_path = "mistralai/Mistral-7B-v0.1"
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    
    # Macedonian test prompts
    test_prompts = [
        "Здраво, јас сум Мистрал, македонски јазичен модел. Можам да",
        "Македонија е земја со богата историја која",
        "Охридското Езеро е познато по",
        "Најважните културни споменици во Македонија се"
    ]
    
    print("\nTesting Mistral-7B responses in Macedonian:")
    print("-" * 50)
    
    for prompt in test_prompts:
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(
            **inputs,
            max_length=200,
            num_return_sequences=1,
            temperature=0.8,
            top_p=0.9,
            do_sample=True
        )
        
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"\nPrompt: {prompt}")
        print(f"Response: {generated_text}")
        print("-" * 50)

if __name__ == "__main__":
    print("Loading Mistral-7B model for Macedonian language testing...")
    load_and_test_model()