# Evaluate fine tune model
from datasets import load_dataset
from transformers import TFMT5ForConditionalGeneration, MT5Tokenizer, DataCollatorForSeq2Seq
from torch.utils.data import DataLoader
import evaluate
import torch
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

dataset = load_dataset("csv", data_files={'train': 'train.csv', 'test': 'test.csv'})
dataset = dataset["test"].shuffle(seed=42)

checkpoint_filepath = "/content/drive/MyDrive/training/2023-11-10/T5.ckpt"
tokenizer = MT5Tokenizer.from_pretrained("google/mt5-small")
model = TFMT5ForConditionalGeneration.from_pretrained("google/mt5-small")
# model.to(device)
model.load_weights(checkpoint_filepath)

def preprocess_function(examples):
    padding = "max_length"
    max_length = 200

    inputs = [ex for ex in examples["Text"]]
    targets = [ex for ex in examples["Expected"]]
    model_inputs = tokenizer(inputs, max_length=max_length, padding=padding, truncation=True)
    labels = tokenizer(targets, max_length=max_length, padding=padding, truncation=True)

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

test_dataset = dataset.map(preprocess_function, batched=True, desc="Running tokenizer")

eval_dataloader = DataLoader(test_dataset, batch_size=8)

model.compile()

def test(test):

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(test)

    # Convert text to sequences of numerical indices
    sequences = tokenizer.texts_to_sequences(test)

    # Pad sequences to ensure they have the same length
    max_sequence_length = 100  # Adjust based on your model's requirements
    return pad_sequences(sequences, maxlen=max_sequence_length)
# metric = evaluate.load("accuracy")
model.evaluate(test(x_test), test(y_test))
# for batch in eval_dataloader:
#     batch = {k: v.to(device) for k, v in batch.items()}
#     with torch.no_grad():
#         outputs = model(**batch)

#     logits = outputs.logits
#     predictions = torch.argmax(logits, dim=-1)
#     metric.add_batch(predictions=predictions, references=batch["labels"])
# metric.compute()
