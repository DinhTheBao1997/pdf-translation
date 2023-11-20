from datasets import load_dataset, DatasetDict
import pandas as pd

# Source: https://huggingface.co/datasets/alt
dataset: DatasetDict = load_dataset('alt')
df = pd.DataFrame(dataset["train"])  # Assuming "train" is a split in your dataset

# Save the DataFrame to a CSV file
df.to_csv("output_file.csv", index=False)
