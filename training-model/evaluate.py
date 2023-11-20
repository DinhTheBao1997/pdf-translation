# Evaluate fine tune model
from datasets import load_dataset
from transformers import TFMT5ForConditionalGeneration, MT5Tokenizer
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

IS_LOAD_FINE_TUNE = False
max_length = 200

dataset = load_dataset("csv", data_files={'train': 'train.csv', 'test': 'test.csv'})
dataset = dataset["test"].shuffle(seed=42)

tokenizer = MT5Tokenizer.from_pretrained("google/mt5-small")
model = TFMT5ForConditionalGeneration.from_pretrained("google/mt5-small")

def preprocess_function(examples):
    padding = "max_length"
    inputs = [ex for ex in examples["Text"]]
    targets = [ex for ex in examples["Expected"]]
    model_inputs = tokenizer(inputs, max_length=max_length, padding=padding, truncation=True)
    labels = tokenizer(targets, max_length=max_length, padding=padding, truncation=True)
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

def to_pad_sequences(test):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(test)
    sequences = tokenizer.texts_to_sequences(test)
    return pad_sequences(sequences, maxlen=max_length)

test_dataset = dataset.map(preprocess_function, batched=True, desc="Running tokenizer")

x = test_dataset['labels']
y = test_dataset['input_ids']
x_test, _, y_test, _ = train_test_split(x, y, test_size=0.75, random_state=42)

IS_LOAD_FINE_TUNE = True
if IS_LOAD_FINE_TUNE:
    checkpoint_filepath = "/content/drive/MyDrive/training/2023-11-10/T5.ckpt"
    model.load_weights(checkpoint_filepath)

def prefix():
    task_prefix = "translate English to German: "
    sentences = ["The house is wonderful.", "I like to work in NYC."]
    inputs = tokenizer([task_prefix + sentence for sentence in sentences], return_tensors="pt", padding=True)
    output_sequences = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        do_sample=False,  # disable sampling to test if batching affects output
    )
    print(tokenizer.batch_decode(output_sequences, skip_special_tokens=True))

def evaluate():
    model.compile()
    # Assuming you have a simple model
    results = model.evaluate(x_test, y_test)

