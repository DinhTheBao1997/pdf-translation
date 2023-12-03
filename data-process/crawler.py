import requests
from bs4 import BeautifulSoup
import csv
from variable import train_urls
import re

def isIgnore(v: str):
    if v is None or len(v) == 0:
        return True
    if re.search("^[\d]+\.", v) is None:
        return False
    return True

def crawler():
    file_name = "CRITICAL CARE MEDICINE"
    urls = train_urls

    queries = [
        "div.topic__accordion>div.para>p",
        "div.topic__accordion> section div.topic__content div.list .topic__listitem",
        "div.topic__accordion> section div.topic__content>div.para>p"
    ]
    def extract_text(elements, lst: list[str]):
        for element in elements:
            text = element.text.strip()
            if (isIgnore(text)):
                continue
            lst.append(text)

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
        writer.writerow(["vi", "en", "ja"])

    def save_csv(texts_en: list[str], texts_vi: list[str], texts_ja: list[str], url):
        if len(texts_en) != len(texts_ja) or len(texts_en) != len(texts_vi):
            return
        length = len(texts_en)
        with open(file_path, 'a', encoding="utf-8") as file:
            writer = csv.writer(file,lineterminator="\n")
            for i in range(0, length):
                writer.writerow([texts_vi[i], texts_en[i], texts_ja[i]])

    # Run the crawler function
    for url in urls:
        texts_en = crawler(url, "en")
        texts_vi = crawler(url, "vi")
        texts_ja = crawler(url, "ja")
        save_csv(texts_en, texts_vi, texts_ja, url["en"])

crawler()
