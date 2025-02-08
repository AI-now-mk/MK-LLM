
# Script to tokenize cleaned text using SentencePiece

import sentencepiece as spm

INPUT_FILE = "data/processed/mk_wiki_clean.txt"
MODEL_PREFIX = "data/tokenized/mk_tokenizer"

def train_tokenizer():
    spm.SentencePieceTrainer.train(input=INPUT_FILE, model_prefix=MODEL_PREFIX, vocab_size=32000)
    print(f"✅ Tokenizer model saved at {MODEL_PREFIX}.model")

if __name__ == "__main__":
    train_tokenizer()
