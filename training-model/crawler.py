import requests
from bs4 import BeautifulSoup, element, ResultSet
import csv
from variable import train_urls, test_urls
# nltk.download('punkt')

def crawler(train_mode):
    if train_mode:
        file_name = "train"
        urls = train_urls
    else:
        file_name = "test"
        urls = test_urls

    queries = [
        ".topic__header--subsection",
        ".para>p"
    ]
    def extract_text(elements: ResultSet[element.Tag], lst: list[str], mode: str):
        for element in elements:
            tooltip = element.select(".tooltip-container")
            if len(tooltip) != 0:
                element = tooltip[0].select(".tooltip-content")[0]
            paragraph: str = element.text
            lst.append(paragraph.strip())

    def crawler(url, mode: str):
        texts = []
        response = requests.get(url[mode])
        text = response.text

        # Parse the HTML content
        soup = BeautifulSoup(text, "html.parser")
        for query in queries:
            elements = soup.select(query)
            extract_text(elements, texts, mode)
        return texts


    file_path = f'data/{file_name}.csv'
    with open(file_path, 'w', encoding="utf-8") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(["en", "vi", "ja", "url"])

    def save_csv(texts_en: list[str], texts_vi: list[str], texts_ja: list[str], url):
        length = min(len(texts_en), len(texts_vi), len(texts_ja))
        with open(file_path, 'a', encoding="utf-8") as file:
            writer = csv.writer(file,lineterminator="\n")
            for i in range(0, length):
                writer.writerow([texts_en[i], texts_vi[i], texts_ja[i], url])

    for url in urls:
        texts_en = crawler(url, "en")
        texts_vi = crawler(url, "vi")
        texts_ja = crawler(url, "ja")
        save_csv(texts_en, texts_vi, texts_ja, url["en"])

for mode in [True, False]:
    crawler(mode)
