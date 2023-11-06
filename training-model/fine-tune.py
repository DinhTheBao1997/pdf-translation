from transformers import AutoTokenizer, BartModel
model = AutoTokenizer.from_pretrained("facebook/bart-base")
tokenizer = BartModel.from_pretrained("facebook/bart-base")
text = "Bhutan begins biggest vaccination drive against Covid-19"
model_inputs = tokenizer(text, return_tensors = "pt")
generated_tokens = model.generate(**model_inputs, forced_bos_token_id = tokenizer.lang_code_to_id ["vi_VN"])
translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
print(translation)
