import os
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1" # Enables fallback to CPU if an operation is not supported by MPS

import torch

if torch.backends.mps.is_available():
    mps_device = torch.device("mps")
    print(f"Using MPS device: {mps_device}")
else:
    print("MPS device not found. Falling back to CPU.")
    mps_device = torch.device("cpu")

from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "HuggingFaceTB/SmolLM2-360M-Instruct" # Example model, choose your desired model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(mps_device)

prompt = "Tell me a story"
inputs = tokenizer(prompt, return_tensors="pt").to(mps_device)

outputs = model.generate(inputs.input_ids, max_new_tokens=100)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(f"Generated text: {generated_text}")
