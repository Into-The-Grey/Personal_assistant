from transformers import AutoModelForCausalLM, AutoTokenizer

# Load tokenizer and model from save directory
tokenizer = AutoTokenizer.from_pretrained("./models/phi-2")
model = AutoModelForCausalLM.from_pretrained("./models/phi-2")
