import csv
import datasets

dataset = datasets.load_dataset("csv", data_files="./data/train.csv")
train = dataset["train"]
file_name="GASTROINTESTINAL DISORDERS"
file_path = f'clean/{file_name}.csv'
with open(file_path, 'w', encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerow(["vi", "en", "ja"])
replacements = [
    {
        "（": "("
    },
    {
        "）": ")"
    },
    {
        "，": ","
    },
    {
        "。": "."
    },
]
def replace(v: str):
    pass

def save_csv():
    with open(file_path, 'a', encoding="utf-8") as file:
        writer = csv.writer(file,lineterminator="\n")
        for data in train:
            vi_text = data["vi"]
            en_text = data["en"]
            ja_text = data["ja"]
            writer.writerow([vi_text, en_text, ja_text])
save_csv()
