# from transformers import MBartForConditionalGeneration, MBartTokenizer
import evaluate
import common
bleu = evaluate.load('bleu')

def func(v):
    return [v]
# predictions = common.read_file("./eval/predictions.en")
predictions = common.read_file("./eval/predictions.ja")
refes = common.read_file("./eval/references.txt")
references=[[v] for v in refes]
# Japanese to English
# lst = []
# predictions=[]
# references=[]
# for eval in eval_data:
#     translation = eval["translation"]
#     src_text = translation[src]
#     tgt_text = translation[tgt]
#     inputs = tokenizer(src_text, return_tensors="pt")
#     translated_tokens = model.generate(**inputs, decoder_start_token_id=tokenizer.lang_code_to_id[lang_code[tgt]], early_stopping=True, max_length=32)
#     pred = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
#     predictions.append(pred)
#     references.append([tgt_text])
results = bleu.compute(predictions=predictions, references=references)
print(results)
