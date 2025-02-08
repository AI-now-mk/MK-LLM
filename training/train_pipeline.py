
# Training pipeline to fine-tune different LLMs

from transformers import Trainer, TrainingArguments

def train_model(model, dataset, tokenizer, output_dir="./models/fine_tuned"):
    training_args = TrainingArguments(
        output_dir=output_dir,
        per_device_train_batch_size=2,
        evaluation_strategy="epoch",
        num_train_epochs=3,
        fp16=True
    )
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        tokenizer=tokenizer,
    )
    trainer.train()
    trainer.save_model(output_dir)
    print(f"✅ Model fine-tuned and saved at {output_dir}")

if __name__ == "__main__":
    print("Training pipeline ready! Call train_model() to start training.")
