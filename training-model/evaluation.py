!pip install -q transformers sentencepiece datasets accelerate evaluate

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

model_repo = "facebook/mbart-large-cc25"
data_files={
    'train': root + 'data/train.csv',
}
dirs = {
    "cache_dir": root + "cache",
    "output_dir": root + "output",
    "logs_dir": root + "logs",
    # "store_model": root + "store_model",
    "store_model": root + "store_model_v1",
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
src = lang_config["src"]
tgt = lang_config["tgt"]
store_model=dirs["store_model"]
print([store_model, src, tgt])

# Hyperparameters
batch_size = 2
learning_rate = 0.003
epochs = 3
split=0.9

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
