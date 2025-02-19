from data_loader import load_mk_dataset

def test_dataset():
    print("Testing Macedonian dataset loader...")
    
    # Load the dataset
    dataset = load_mk_dataset()
    
    # Print basic statistics
    print(f"\nDataset size: {len(dataset)} examples")
    
    # Show first few examples
    print("\nFirst 3 examples:")
    for i in range(min(3, len(dataset))):
        text = dataset[i]['text']
        print(f"\nExample {i+1}:")
        print(f"Length: {len(text)} characters")
        print(f"Preview: {text[:200]}...")  # Show first 200 characters

if __name__ == "__main__":
    test_dataset()