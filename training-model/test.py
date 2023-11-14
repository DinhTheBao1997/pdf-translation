# Run fine tune model
from datasets import load_dataset

dataset = load_dataset("csv", data_files={'train': 'train.csv', 'test': 'test.csv'})
dataset = dataset["test"].shuffle(seed=42)
