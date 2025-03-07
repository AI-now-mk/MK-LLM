
# Enhanced training pipeline with multi-GPU support

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from datasets import load_dataset

MODEL_NAME = "mistralai/Mistral-7B-v0.1"
DATASET_PATH = "data/tokenized/mk_wiki_tokenized.txt"
OUTPUT_DIR = "./models/mistral-multi-gpu"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
dataset = load_dataset("text", data_files={"train": DATASET_PATH})

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16,
    device_map="auto"  # Automatically distribute model across multiple GPUs
)

training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=2,
    evaluation_strategy="epoch",
    num_train_epochs=3,
    fp16=True,
    save_total_limit=2,
    logging_dir="./logs",
    report_to="none"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    tokenizer=tokenizer,
)

if __name__ == "__main__":
    trainer.train()
    trainer.save_model(OUTPUT_DIR)
    print(f"✅ Multi-GPU fine-tuning complete! Model saved at {OUTPUT_DIR}")
