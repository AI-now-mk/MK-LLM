import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def test_local_model():
    print("Loading base model...")
    
    # Use XLM-RoBERTa model for better Slavic language support
    model_name = "xlm-roberta-large"
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="cpu",
        torch_dtype=torch.float32
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # More specific Macedonian prompts
    test_prompts = [
        "<mk>Здраво, јас сум од Македонија. Како си ти?</mk>",
        "<mk>Скопје е главен град на Македонија. Опиши го градот.</mk>",
        "<mk>Охридското Езеро е најголемото езеро во Македонија. Кажи ми повеќе за него.</mk>",
        "<mk>Опиши ја македонската култура и традиција.</mk>"
    ]
    
    print("\nGenerating responses in Macedonian...")
    for prompt in test_prompts:
        print(f"\nPrompt: {prompt}")
        
        inputs = tokenizer(
            prompt, 
            return_tensors="pt", 
            max_length=512, 
            truncation=True,
            add_special_tokens=True
        )
        outputs = model.generate(
            **inputs,
            max_length=150,
            num_return_sequences=1,
            temperature=0.7,  # Reduced for more focused responses
            do_sample=True,
            top_p=0.92,
            no_repeat_ngram_size=3,
            pad_token_id=tokenizer.pad_token_id,
            bos_token_id=tokenizer.bos_token_id,
            eos_token_id=tokenizer.eos_token_id
        )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"Response: {response}\n")
        print("-" * 50)

if __name__ == "__main__":
    test_local_model()