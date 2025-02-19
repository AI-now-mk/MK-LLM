import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from datasets import Dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from huggingface_hub import login

def setup_mistral(token):
    model_name = "mistralai/Mistral-7B-v0.1"
    
    # Add model configuration
    model_config = {
        "load_in_4bit": True,
        "device_map": "auto",
        "token": token,
        "trust_remote_code": True,
        "max_memory": {0: "24GB"},  # Adjust based on GPU
        "torch_dtype": torch.float16
    }
    
    model = AutoModelForCausalLM.from_pretrained(model_name, **model_config)
    tokenizer = AutoTokenizer.from_pretrained(model_name, token=token)
    return model, tokenizer
    
def train_mistral(token):
    model, tokenizer = setup_mistral(token)
    
    training_args = TrainingArguments(
        output_dir="./models/mistral-mk",
        num_train_epochs=3,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        learning_rate=2e-4,
        fp16=True,
        save_steps=100,
        logging_steps=10,
        max_steps=2000
    )
    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=load_mk_dataset(),  # You'll need to implement this
        tokenizer=tokenizer
    )
    
    trainer.train()
    trainer.save_model("./models/mistral-mk")
    print("✅ Mistral-7B fine-tuning complete!")

if __name__ == "__main__":
    print("Starting Mistral-7B fine-tuning for Macedonian...")
    # Replace with your Hugging Face token
    token = "your_token_here"
    train_mistral(token)