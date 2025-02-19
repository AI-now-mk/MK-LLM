import os
import json
import random
from transformers import AutoModelForCausalLM, AutoTokenizer

def test_prompts():
    print("Loading model and data...")
    
    # Load model and tokenizer
    model_name = "facebook/opt-350m"  # Using smaller model for testing
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="cpu")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Load collected data
    cleaned_data = os.path.join("data", "cleaned", "mk_combined_data.txt")
    with open(cleaned_data, 'r', encoding='utf-8') as f:
        texts = f.read().split('\n\n')
    
    print(f"\nLoaded {len(texts)} text samples")
    
    # Interactive prompt testing
    while True:
        print("\n" + "="*50)
        print("Options:")
        print("1. See random sample from data")
        print("2. Test custom prompt")
        print("3. Generate response to sample")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            sample = random.choice(texts)
            print("\nRandom sample:")
            print("-" * 30)
            print(sample[:500] + "..." if len(sample) > 500 else sample)
        
        elif choice == '2':
            prompt = input("\nEnter your prompt in Macedonian: ")
            inputs = tokenizer(prompt, return_tensors="pt")
            outputs = model.generate(
                **inputs,
                max_length=100,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True
            )
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            print("\nResponse:")
            print("-" * 30)
            print(response)
        
        elif choice == '3':
            sample = random.choice(texts)
            print("\nSample context:")
            print("-" * 30)
            print(sample[:200] + "...")
            
            inputs = tokenizer(sample[:500], return_tensors="pt")
            outputs = model.generate(
                **inputs,
                max_length=150,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True
            )
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            print("\nGenerated continuation:")
            print("-" * 30)
            print(response)
        
        elif choice == '4':
            print("\nExiting...")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    test_prompts()