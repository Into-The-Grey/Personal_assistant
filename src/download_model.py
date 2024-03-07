from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "microsoft/phi-2"
save_directory = "./models/phi-2"  # Update this path to your desired save location

# Download and save tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.save_pretrained(save_directory)

# Download and save model
model = AutoModelForCausalLM.from_pretrained(model_name)
model.save_pretrained(save_directory)
