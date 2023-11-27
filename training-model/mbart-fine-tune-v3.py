!pip install -q transformers sentencepiece datasets accelerate sklearn

from transformers import MBartForConditionalGeneration, MBartTokenizer
import math
from transformers import Seq2SeqTrainingArguments, Seq2SeqTrainer
import datasets
import os
import shutil
from google.colab import drive

drive.mount('/content/drive')
# %cd /content/drive/MyDrive/
root="/content/drive/MyDrive/"

# Hyperparameters
batch_size = 1
learning_rate = 0.003
epochs = 1
split=0.9
max_length=32

model_repo = "facebook/mbart-large-cc25"
data_files={
    'train': 'data/train.csv',
}
dirs = {
    "cache_dir": root + "cache",
    "output_dir": root + "output",
    "logs_dir": root + "logs",
    "store_model": root + "store_model",
}
lang_config = {
    "src": "ja",
    "tgt": "en"
}
lang_code = {
    "ja": "ja_XX",
    "en": "en_XX",
    "vi": "vi_VN",
}
src = lang_config["src"]
tgt = lang_config["tgt"]

def create_folder():
    folders = list(dirs.values())
    for folder in folders:
        print(folder)
        if os.path.exists(folder):
            shutil.rmtree(folder)
        if not os.path.exists(folder):
            os.makedirs(folder)
create_folder()

def load_model():
    model = MBartForConditionalGeneration.from_pretrained(model_repo)
    model.save_pretrained(dirs["store_model"])
    model = MBartForConditionalGeneration.from_pretrained(dirs["store_model"])
    return model

def load_tokenizer():
    tokenizer = MBartTokenizer.from_pretrained(model_repo, src_lang=lang_code[src], tgt_lang=lang_code[tgt])
    tokenizer.save_pretrained(dirs["store_model"])
    tokenizer = MBartTokenizer.from_pretrained(dirs["store_model"])
    return tokenizer

def load_data_set() -> datasets.arrow_dataset.Dataset:
    dataset = datasets.load_dataset("csv", data_files=data_files, cache_dir=dirs["cache_dir"])
    return dataset["train"]

def create_dataset():
    lst_data = load_data_set()
    train_data = []
    for data in lst_data:
        dic = {}
        dic[src] = data[src]
        dic[tgt] = data[tgt]
        train_data.append({"translation": dic})
    return train_data

def create_data_train():
    raw_data = create_dataset()
    train_length = math.floor(split * len(raw_data))
    train_data = raw_data[:train_length]
    eval_data = raw_data[train_length:]
    print(f"raw_data size: {len(raw_data)}")
    print(f"train_data size: {len(train_data)}")
    print(f"eval_data size: {len(eval_data)}")
    return train_data, eval_data

def repair() -> Seq2SeqTrainer:
    train_data, eval_data = create_data_train()
    model = load_model()
    tokenizer = load_tokenizer()


    def data_collator(features: list):
        input_label = [f["translation"][src] for f in features]
        output_label = [f["translation"][tgt] for f in features]
        print(f"input_label: {len(input_label[0])}")
        print(f"output_label: {len(output_label[0])}")
        inputs = tokenizer(input_label, return_tensors="pt", padding='max_length', truncation=True, max_length=max_length)
        with tokenizer.as_target_tokenizer():
            inputs['labels'] = tokenizer(output_label, return_tensors="pt", padding='max_length', truncation=True, max_length=max_length)['input_ids']
        return inputs

    args = Seq2SeqTrainingArguments(output_dir=dirs["output_dir"],
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
    output_dir=dirs["store_model"]
    trainer.train()
    trainer.save_model(output_dir)

    model = MBartForConditionalGeneration.from_pretrained(output_dir)
    tokenizer = MBartTokenizer.from_pretrained(output_dir)

    sentence = "行っていいのですか?"
    inputs = tokenizer(sentence, return_tensors="pt")
    translated_tokens = model.generate(**inputs, decoder_start_token_id=tokenizer.lang_code_to_id["en_XX"], early_stopping=True, max_length=max_length)
    pred = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
    print(type(translated_tokens))
    print(f"日本語 - {sentence}: English - {pred}")

trainer = repair()
run(trainer)

model = MBartForConditionalGeneration.from_pretrained(output_dir)
tokenizer = MBartTokenizer.from_pretrained(output_dir)
results = model.eval()
