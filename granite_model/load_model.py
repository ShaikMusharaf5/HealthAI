from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "ibm-granite/granite-3.3-2b-instruct"
hf_token = "hf_xxxYourTokenHerexxx"    # paste your hugging face token here before running the code

tokenizer = AutoTokenizer.from_pretrained(model_id, token=hf_token)
model = AutoModelForCausalLM.from_pretrained(model_id, token=hf_token, torch_dtype=torch.float32)

# Optional test code
if __name__ == "__main__":
    prompt = "Suggest natural home remedies for cold and cough"
    inputs = tokenizer(prompt, return_tensors="pt")
    
    # Add attention_mask to avoid empty output
    if "attention_mask" not in inputs:
        inputs["attention_mask"] = torch.ones_like(inputs["input_ids"])

    outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_new_tokens=60,
        do_sample=True,         # Sampling enabled
        temperature=0.7,        # Adds variation
        top_p=0.9               # Top-p sampling
    )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("🧠 Assistant:", response)

