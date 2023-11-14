import requests
from bs4 import BeautifulSoup
import csv
from variable import train_urls, test_urls
import hashlib

train_mode = False
result = {}

if train_mode:
    file_name = "train"
    urls = train_urls
else:
    file_name = "test"
    urls = test_urls

file_path = f'data/{file_name}.csv'
with open(file_path, 'w', encoding="utf-8") as file:
    writer = csv.writer(file,lineterminator="\n")
    writer.writerow(["Id", "Language", "Text", "Expected"])

origin = "https://www.msdmanuals.com"
def crawler(url, mode: str):
    texts = []
    response = requests.get(url[mode])
    text = response.text

    # Parse the HTML content
    soup = BeautifulSoup(text, "html.parser")
    nodeList = soup.find_all(class_="para")
    for node in nodeList:
        text: str = node.text
        texts.append(text.strip())
    result[mode] = texts

def save_csv():
    texts_en = result["en"]
    texts_vi = result["vi"]
    if len(texts_en) != len(texts_vi):
        return
    with open(file_path, 'a', encoding="utf-8") as file:
        writer = csv.writer(file,lineterminator="\n")
        for i in range(0, len(texts_en)):
            text_en = texts_en[i]
            id = hashlib.md5(text_en.encode()).hexdigest()
            writer.writerow([id, "en", text_en, texts_vi[i]])

# Run the crawler function

for url in urls:
    crawler(url, "en")
    crawler(url, "vi")
    try:
        save_csv()
    except:
        print(url)
