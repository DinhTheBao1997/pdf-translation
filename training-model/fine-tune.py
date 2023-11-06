from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt", src_lang="en_XX")
text = "Bhutan begins biggest vaccination drive against Covid-19"
model_inputs = tokenizer(text, return_tensors = "pt")
generated_tokens = model.generate(**model_inputs, forced_bos_token_id = tokenizer.lang_code_to_id ["vi_VN"])
translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
print(translation)
