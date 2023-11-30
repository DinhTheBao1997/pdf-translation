def data_collator(features: list):
    x = [f["translation"][src] for f in features]
    y = [f["translation"][tgt] for f in features]
    inputs = tokenizer(x, return_tensors="pt", padding='max_length', truncation=True, max_length=32)
    with tokenizer.as_target_tokenizer():
        inputs['labels'] = tokenizer(y, return_tensors="pt", padding='max_length', truncation=True, max_length=48)['input_ids']
    return inputs
