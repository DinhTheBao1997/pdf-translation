!pip install -q transformers sentencepiece datasets accelerate numpy pandas fairseq
!wget "https://nlp.stanford.edu/projects/jesc/data/split.tar.gz"
!tar -zxvf split.tar.gz
!ls split
!mkdir reduced_model
!mkdir output

from fairseq.data import Dictionary
from transformers import (
    MBartForConditionalGeneration, MBartTokenizer, MBartConfig
)
from typing import List
import torch
from transformers import (
    Seq2SeqTrainingArguments, Seq2SeqTrainer
)
import numpy as np
import re
import sentencepiece as spm

result_dir = "./output"

def repair() -> Seq2SeqTrainer:
    # Hyperparameters
    batch_size = 1
    learning_rate = 0.003
    epochs = 1
    res = []
    for line in open('split/train', 'r', encoding='utf-8'):
        text = line.split('\t')[:2000]
        text = [t.rstrip('\n') for t in text]
        res.extend(text)
    for line in open('split/dev', 'r', encoding='utf-8'):
        text = line.split('\t')[:1000]
        text = [t.rstrip('\n') for t in text]
        res.extend(text)
    for line in open('split/test', 'r', encoding='utf-8'):
        text = line.split('\t')[:1000]
        text = [t.rstrip('\n') for t in text]
        res.extend(text)

    print(len(res))
    with open('tmp.txt', 'w') as f:
        for d in res:
            f.write("%s\n" % d)

    model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-cc25")
    tokenizer = MBartTokenizer.from_pretrained("facebook/mbart-large-cc25")

    model.save_pretrained("./reduced_model")
    tokenizer.save_pretrained("./reduced_model")

    model = MBartForConditionalGeneration.from_pretrained("./reduced_model")
    tokenizer = MBartTokenizer.from_pretrained("./reduced_model")


    def data_collator(features: list):
        x = [f["translation"]["ja"] for f in features]
        y = [f["translation"]["en"] for f in features]
        inputs = tokenizer(x, return_tensors="pt", padding='max_length', truncation=True, max_length=32)
        with tokenizer.as_target_tokenizer():
            inputs['labels'] = tokenizer(y, return_tensors="pt", padding='max_length', truncation=True, max_length=48)['input_ids']
        return inputs

    tokenizer = MBartTokenizer.from_pretrained("./reduced_model", src_lang="ja_XX", tgt_lang="en_XX")
    tokenizer.save_pretrained(result_dir)

    train_data = []
    eval_data = []

    for line in open("./split/train", "r", encoding='utf-8'):
        text = line.split('\t')
        train_data.append(
            {"translation": {
                "ja": text[1].rstrip('\n'),
                "en": text[0].rstrip('\n')
            }}
        )
    train_data=train_data[:5000]
    print(f"train_data size: {len(train_data)}")

    for line in open("./split/dev", "r", encoding='utf-8'):
        text = line.split('\t')
        eval_data.append(
            {"translation": {
                "ja": text[1].rstrip('\n'),
                "en": text[0].rstrip('\n')
            }}
        )
    print(f"eval_data size: {len(eval_data)}")

    model = MBartForConditionalGeneration.from_pretrained("./reduced_model")

    args = Seq2SeqTrainingArguments(output_dir=result_dir,
                                    do_train=True,
                                    do_eval=True,
                                    per_device_train_batch_size=batch_size,
                                    per_device_eval_batch_size=batch_size,
                                    learning_rate=learning_rate,
                                    num_train_epochs=epochs,
                                    evaluation_strategy="epoch",
                                    remove_unused_columns=False,
                                    )

    trainer = Seq2SeqTrainer(model=model,
                            args=args,
                            data_collator=data_collator,
                            train_dataset=train_data,
                            eval_dataset=eval_data,
                            )
    return trainer

def run(trainer: Seq2SeqTrainer):
    trainer.train()
    trainer.save_model(result_dir)

    model = MBartForConditionalGeneration.from_pretrained("./output")
    tokenizer = MBartTokenizer.from_pretrained("./output")

    sentence = "行っていいのですか?"
    inputs = tokenizer(sentence, return_tensors="pt")
    translated_tokens = model.generate(**inputs, decoder_start_token_id=tokenizer.lang_code_to_id["en_XX"], early_stopping=True, max_length=48)
    pred = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
    print(type(translated_tokens))
    print(f"日本語 - {sentence}: English - {pred}")

trainer = repair()
run(trainer)
