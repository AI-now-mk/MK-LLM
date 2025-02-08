
# Unit test to verify the model generates responses

from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_PATH = "./models/mistral-finetuned-mk"

def test_model():
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    sample_input = "Што е вештачка интелигенција?"
    inputs = tokenizer(sample_input, return_tensors="pt")
    outputs = model.generate(**inputs)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    assert len(generated_text) > 5, "❌ Model output is too short!"
    print("✅ Model test passed!")

if __name__ == "__main__":
    test_model()
