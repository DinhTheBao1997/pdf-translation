import common
import csv
texts_en = []
texts_vi = []
file_name = "train"
file_path = f'data/{file_name}.csv'

with open(file_path, 'w', encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerow(["en", "vi"])
def save_csv(texts_en: list[str], texts_vi: list[str]):
    length = min(len(texts_en), len(texts_vi))
    with open(file_path, 'a', encoding="utf-8") as file:
        writer = csv.writer(file,lineterminator="\n")
        for i in range(0, length):
            writer.writerow([texts_en[i].strip(), texts_vi[i].strip()])

lines = common.read_file("./data/vie.txt")
for line in lines:
    if len(line) == 0:
        continue
    arr = line.split("\t")
    texts_en.append(arr[0].strip())
    texts_vi.append(arr[1].strip())
save_csv(texts_en, texts_vi)
