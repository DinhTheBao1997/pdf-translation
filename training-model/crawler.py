import requests
from bs4 import BeautifulSoup
import csv
from variable import train_urls, test_urls
import hashlib
import json


def crawler(train_mode):
    if train_mode:
        file_name = "train"
        urls = train_urls
    else:
        file_name = "test"
        urls = test_urls

    queries = [
        ".para .topic__explanation",
        ".topic__header--subsection",
        ".para>p"
    ]
    def extract_text(elements, lst: list[str]):
        for element in elements:
            lst.append(element.text.strip().replace("’", "'"))

    def crawler(url, mode: str):
        texts = []
        response = requests.get(url[mode])
        text = response.text

        # Parse the HTML content
        soup = BeautifulSoup(text, "html.parser")
        for query in queries:
            elements = soup.select(query)
            extract_text(elements, texts)
        return texts


    file_path = f'data/{file_name}.csv'
    with open(file_path, 'w', encoding="utf-8") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(["id", "translation", "url"])

    def save_csv(texts_en: list[str], texts_vi: list[str], texts_ja: list[str], url):
        length = min(len(texts_en), len(texts_vi), len(texts_ja))
        with open(file_path, 'a', encoding="utf-8") as file:
            writer = csv.writer(file,lineterminator="\n")
            for i in range(0, length):
                dic = {
                    'en': texts_en[i],
                    'vi': texts_vi[i],
                    'ja': texts_ja[i],
                }
                text = json.dumps(dic, ensure_ascii=False)
                index = hashlib.md5(url.encode()).hexdigest()
                print([index, text, url])
                writer.writerow([index, text, url])

    # Run the crawler function
    for url in urls:
        texts_en = crawler(url, "en")
        texts_vi = crawler(url, "vi")
        texts_ja = crawler(url, "ja")
        save_csv(texts_en, texts_vi, texts_ja, url["en"])

for mode in [True, False]:
    crawler(mode)
