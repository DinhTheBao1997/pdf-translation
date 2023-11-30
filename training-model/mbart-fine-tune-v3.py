!pip install -q transformers sentencepiece datasets accelerate sklearn

from transformers import MBartForConditionalGeneration, MBartTokenizer
import math
from transformers import Seq2SeqTrainingArguments, Seq2SeqTrainer
import datasets
import os
import shutil
from google.colab import drive

root="/content/drive/MyDrive/"
model_repo = "facebook/mbart-large-cc25"
data_files={
    'train': root + 'data/train.csv',
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
    # "src": "en",
    # "tgt": "vi"
}
lang_code = {
    "ja": "ja_XX",
    "en": "en_XX",
    "vi": "vi_VN",
}
drive.mount('/content/drive')
# %cd /content/drive/MyDrive/
src = lang_config["src"]
tgt = lang_config["tgt"]
store_model=dirs["store_model"]
print([store_model, src, tgt])

# Hyperparameters
batch_size = 2
learning_rate = 0.0005
epochs = 4
logging_steps=1000
save_steps=1000
split=0.9
save_strategy="epoch"

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
    model.save_pretrained(store_model)
    model = MBartForConditionalGeneration.from_pretrained(store_model)
    return model

def load_tokenizer():
    src = lang_config["src"]
    tgt = lang_config["tgt"]
    tokenizer = MBartTokenizer.from_pretrained(model_repo, src_lang=lang_code[src], tgt_lang=lang_code[tgt])
    tokenizer.save_pretrained(store_model)
    tokenizer = MBartTokenizer.from_pretrained(store_model)
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
        x = [f["translation"][src] for f in features]
        y = [f["translation"][tgt] for f in features]
        inputs = tokenizer(x, return_tensors="pt", padding='max_length', truncation=True, max_length=32)
        with tokenizer.as_target_tokenizer():
            inputs['labels'] = tokenizer(y, return_tensors="pt", padding='max_length', truncation=True, max_length=48)['input_ids']
        return inputs

    args = Seq2SeqTrainingArguments(output_dir=dirs["output_dir"],
                                    overwrite_output_dir =True,
                                    do_train=True,
                                    do_eval=True,
                                    evaluation_strategy="epoch",
                                    per_device_train_batch_size=batch_size,
                                    per_device_eval_batch_size=batch_size,
                                    save_steps=save_steps,
                                    save_strategy=save_strategy,
                                    learning_rate=learning_rate,
                                    logging_steps=logging_steps,
                                    num_train_epochs=epochs,
                                    remove_unused_columns=False,
                                )

    trainer = Seq2SeqTrainer(model=model,
                            args=args,
                            data_collator=data_collator,
                            tokenizer=tokenizer,
                            train_dataset=train_data,
                            eval_dataset=eval_data,
                            )
    return trainer

def run(trainer: Seq2SeqTrainer):
    output_dir=store_model
    trainer.train()
    trainer.save_model(output_dir)


def manual_test():
    output_dir=store_model
    model = MBartForConditionalGeneration.from_pretrained(output_dir)
    tokenizer = MBartTokenizer.from_pretrained(output_dir)

    sentence = "上部消化管の愁訴としては以下のものがある"
    inputs = tokenizer(sentence, return_tensors="pt")
    translated_tokens = model.generate(**inputs, decoder_start_token_id=tokenizer.lang_code_to_id[lang_code[lang_config["tgt"]]], early_stopping=True, max_length=48)
    pred = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
    print(type(translated_tokens))
    print(f"日本語 - {sentence}: English - {pred}")
