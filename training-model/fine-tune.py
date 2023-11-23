!pip install -q transformers sentencepiece datasets accelerate

# ================================================ import ================================================
from google.colab import drive
import json
from tokenizers import normalizers, pre_tokenizers, Tokenizer, models, trainers
from transformers import AutoTokenizer, PreTrainedTokenizerFast, MBartForConditionalGeneration, MBartTokenizer
from transformers import BartForConditionalGeneration
from transformers import Seq2SeqTrainingArguments, Seq2SeqTrainer
import datasets
from datasets import Dataset
import os
import torch
from torch.utils.data import random_split
# ================================================ import ================================================

# ================================================ config ================================================
drive.mount('/content/drive')
%cd /content/drive/MyDrive/
root="/content/drive/MyDrive/"
dirs = {
    "cache_dir": root + "cache",
    "output_dir": root + "output",
    "logs_dir": root + "logs",
}

model_repo = "facebook/mbart-large-cc25"
data_files={
    'train': 'data/train.csv',
    'test': 'data/test.csv',
    'validation': 'data/validation.csv'
}
langs = {
    "en": "en_XX",
    "vi": "vi_VN",
    "ja": "ja_XX",
}
src="en"
tat="vi"
split = 0.9
folders = list(dirs.keys())

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

dataset = datasets.load_dataset("csv", data_files=data_files, cache_dir=dirs["cache_dir"])
model = BartForConditionalGeneration.from_pretrained(model_repo)

def flatten(batch):
    translation = json.loads(batch['translation'])
    batch['en'] = translation['en']
    batch['vi'] = translation['vi']
    batch['ja'] = translation['ja']

    return batch

# Map the 'flatten' function
train = dataset['train'].map(flatten)
test = dataset['test'].map(flatten)
validation = dataset['validation'].map(flatten)

# Save to disk
train.save_to_disk("./dataset/train")
test.save_to_disk("./dataset/test")
validation.save_to_disk("./dataset/validation")
# ================================================ config ================================================


# ================================================ version 1 start ================================================
# Build a tokenizer
def fine_tune_v1():
    bpe_tokenizer = Tokenizer(models.BPE())
    bpe_tokenizer.normalizer = normalizers.Lowercase()
    bpe_tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()

    trainer = trainers.BpeTrainer(
        vocab_size=50265,
        special_tokens=["<s>", "<pad>", "</s>", "<unk>", "<mask>"],
        initial_alphabet=pre_tokenizers.ByteLevel.alphabet(),
    )

    en_tokenizer = AutoTokenizer.from_pretrained(model_repo)
    vi_tokenizer = PreTrainedTokenizerFast.from_pretrained( "./vi_tokenizer.json" )
    vi_tokenizer.pad_token = en_tokenizer.pad_token

    def tokenize_dataset(sample):
        input = en_tokenizer(sample['en'], padding='max_length', max_length=120, truncation=True)
        label = vi_tokenizer(sample['vi'], padding='max_length', max_length=120, truncation=True)

        input["decoder_input_ids"] = label["input_ids"]
        input["decoder_attention_mask"] = label["attention_mask"]
        input["labels"] = label["input_ids"]

        return input

    train_tokenized = train.map(tokenize_dataset, batched=True)
    validation_tokenized = validation.map(tokenize_dataset, batched=True)

    training_args = Seq2SeqTrainingArguments(
        output_dir="./cache",
        evaluation_strategy="steps",
        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,
        predict_with_generate=True,
        logging_steps=2,  # set to 1000 for full training
        save_steps=64,  # set to 500 for full training
        eval_steps=64,  # set to 8000 for full training
        warmup_steps=1,  # set to 2000 for full training
        max_steps=128, # delete for full training
        overwrite_output_dir=True,
        save_total_limit=3,
        fp16=False, # True if GPU
    )

    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=train_tokenized,
        eval_dataset=validation_tokenized,
    )

    trainer.train()
# ================================================ version 1 end ================================================

# ================================================ version 2 start ================================================
def fine_tune_v2():
    model = MBartForConditionalGeneration.from_pretrained(model_repo)
    tokenizer = MBartTokenizer.from_pretrained(model_repo)
    tokenizer.save_pretrained(dirs["output_dir"])

    def create_data():
        listData = [train, test]
        data = []
        for lst in listData:
            for i in range(0, len(lst)):
                data.append(json.loads(lst[i]["translation"]))
        return data

    def data_collator(features:list):
        labels = [f["translation"][src] for f in features]
        inputs = [f["translation"][tat] for f in features]

        batch = tokenizer.prepare_seq2seq_batch(
            src_texts=inputs,
            tgt_texts=labels,
            src_lang=langs[src],
            tgt_lang=langs[tat],
            max_length=32,
            max_target_length=32
        )
        for k in batch:
            batch[k] = torch.tensor(batch[k])
        return batch

    data = create_data()
    print(f'total size of data is {len(data)}')

    train_dataset, eval_dataset = random_split(data, lengths=[int((1-split)*len(data))+1, int(split*len(data))])

    args = Seq2SeqTrainingArguments(output_dir=dirs["output_dir"],
                            do_train=True,
                            per_device_train_batch_size=16,
                            learning_rate=5e-2,
                            num_train_epochs=1,
                            remove_unused_columns=False,
                            logging_dir=dirs["logs_dir"]
                            )
    trainer = Seq2SeqTrainer(model=model, 
                    args=args, 
                    data_collator=data_collator, 
                    train_dataset=train_dataset, 
                    eval_dataset=eval_dataset)

    trainer.train()
# ================================================ version 2 end ================================================


# ================================================ training start ================================================
fine_tune_v2()
# ================================================ training end ================================================
