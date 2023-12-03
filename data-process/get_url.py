import requests
from bs4 import BeautifulSoup
import csv
import re
import json
import common
import time

root_url="https://www.msdmanuals.com"
topic_links_file = "./crawling/health-topics.link"
base_detail_links_file="./crawling/jp-detail-links/link.jp"

topics_query = ".section__list--2col a"
details_query = ".medicalsection.main__content>.medicalsection__main>ul>li>div.medicalsection__column>ul>li>a"
lang_link_query = ".langswitcher__selector>option"

crawler_queries = [
        "div.topic__accordion>div.para>p",
        "div.topic__accordion> section div.topic__content div.list .topic__listitem",
        "div.topic__accordion> section div.topic__content>div.para>p"
    ]

def read_file(path):
    data = ""
    with open(path, 'r', encoding='utf-8') as f:
        data = f.readlines()
    return data

def join(lst):
    return json.loads("".join(lst))

def get_detail_links_url(url: str):
    links = []
    response = requests.get(url)
    text = response.text
    # Parse the HTML content
    soup = BeautifulSoup(text, "html.parser")
    elements = soup.select(details_query)
    for element in elements:
        href = element.attrs["href"]
        detail_url=root_url+href
        links.append(detail_url)
    return links

def get_detail_links():
    results = []
    topic_links = join(read_file(topic_links_file))
    # topic_links=topic_links[:1]
    for topic_link in topic_links:
        print(topic_link)
        links = get_detail_links_url(topic_link)
        results.extend(links)
    common.write_file("./crawling/jp-detail-links/link.jp", json.dumps(results, indent=4, ensure_ascii=False))

def get_language_link(url: str, contain: str):
    links = []
    response = requests.get(url)
    text = response.text
    # Parse the HTML content
    soup = BeautifulSoup(text, "html.parser")
    elements = soup.select(lang_link_query)
    # common.write_file("test.html", text)
    for element in elements:
        value = element.attrs["value"]
        # detail_url=root_url+href
        if contain in value:
            return root_url + value
        # links.append(detail_url)
    # return links

def crawler_text():
    def isIgnore(v: str):
        if v is None or len(v) == 0:
            return True
        if re.search("^[\d]+\.", v) is None:
            return False
        return True
    def extract_text(elements, lst: list[str]):
        for element in elements:
            text = element.text.strip()
            if (isIgnore(text)):
                continue
            lst.append(text)
    def crawler(url: str):
        texts = []
        if url is None or len(url.strip()) == 0:
            return []
        response = requests.get(url)
        if response.status_code != 200:
            return []
        text = response.text

        # Parse the HTML content
        soup = BeautifulSoup(text, "html.parser")
        for query in crawler_queries:
            elements = soup.select(query)
            extract_text(elements, texts)
        return texts
    file_name="crawler"
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
    link_file = "./crawling/links/link.txt"
    length=1000
    def get_urls():
        base_links = join(read_file(base_detail_links_file))
        base_links = base_links[:length]
        urls = []
        for link in base_links:
            link_dic = {
                "vi": "",
                "en": "",
                "ja": link,
            }
            for i in range(0, len(langs_1)):
                url = get_language_link(link, langs_1[i])
                link_dic[langs_2[i]]=url
            urls.append(link_dic)
        common.write_file(link_file, json.dumps(urls, indent=4, ensure_ascii=False))
        # urls = join(common.read_file(link_file))
        return urls


    langs_1 =["newLanguage=vi", "newLanguage=en-"]
    langs_2 = ["vi", "en"]

    print("get_urls start")
    start=time.time()
    urls=get_urls()
    end=time.time()
    print(f'url time: {end - start}')
    print("get_urls end")

    for url in urls:
        texts_en = crawler(url["en"])
        texts_vi = crawler(url["vi"])
        texts_ja = crawler(url["ja"])
        url["ja"]
        save_csv(texts_en, texts_vi, texts_ja, url["en"])
    return urls
print("crawler_text start")
start=time.time()
crawler_text()
end=time.time()
print(f'time: {end - start}')
print("crawler_text end")
