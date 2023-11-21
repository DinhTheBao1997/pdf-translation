
import json
import csv
source_file_path = 'data/train.en'
target_file_path = 'data/train.vi'

# Read the contents of source and target files
with open(source_file_path, 'r', encoding='utf-8') as source_file:
    source_lines = source_file.readlines()

with open(target_file_path, 'r', encoding='utf-8') as target_file:
    target_lines = target_file.readlines()

# Remove newline characters and create a list of pairs
dataset = list(zip(source_lines, target_lines))

file_name = "en-vi"
file_path = f'data/{file_name}.csv'
with open(file_path, 'w', encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerow(["id", "translation"])

# Display the resulting dataset
i = 1
with open(file_path, 'a', encoding="utf-8") as file:
    writer = csv.writer(file,lineterminator="\n")
    for pair in dataset:
        source_text, target_text = pair
        dic = {
            'en': source_text.strip(),
            'vi': target_text.strip(),
        }
        text = json.dumps(dic, ensure_ascii=False)
        writer.writerow([i, text])
        i += 1
