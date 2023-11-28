import csv
import os
import datasets
import common
import re

folder="./clean"
file_name="clean"
file_path = f'test/{file_name}.csv'
results = []
def isEmpty(*args: str):
    for arg in args:
        if arg is None or len(arg) == 0:
            return True
    return False

def isIgnore(v: str):
    if re.search("^[\d]+\.", v) is None:
        return False
    return True

for name in os.listdir(folder):
    if name == "clean.csv":
        continue
    file = os.path.join(folder, name)
    dataset = datasets.load_dataset("csv", data_files=file)
    results.extend(list(dataset["train"]))
results=results[:200]
def save_csv():
    with open(file_path, 'w', encoding="utf-8") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(["vi", "en", "ja"])
    with open(file_path, 'a', encoding="utf-8") as file:
        writer = csv.writer(file,lineterminator="\n")
        for data in results:
            en_text = data["en"]
            if isIgnore(en_text):
                continue
            vi_text = data["vi"]
            ja_text = data["ja"]
            if isEmpty(vi_text, en_text, ja_text):
                continue
            writer.writerow([vi_text, en_text, ja_text])
save_csv()

