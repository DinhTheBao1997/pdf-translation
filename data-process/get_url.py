import requests
from bs4 import BeautifulSoup
import csv
import re
import json
import time

root_url="https://www.msdmanuals.com"
topic_links_file = "./crawling/health-topics.link"
base_detail_links_file="./crawling/detail-links.en"
link_file = "./crawling/link.txt"
length=1

lang_conf = {
    "en": "",
    "vi": "newLanguage=vi",
    "fr": "newLanguage=fr",
    "es": "newLanguage=es",
}

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
def write_file(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)
def join(lst):
    return json.loads("".join(lst))

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
    write_file(base_detail_links_file, json.dumps(results, indent=4, ensure_ascii=False))

def crawler_text():
    file_name="crawler"
    file_path = f'data/{file_name}.csv'

    def get_language_link(url: str, contain: str):
        response = requests.get(url)
        text = response.text
        soup = BeautifulSoup(text, "html.parser")
        elements = soup.select(lang_link_query)

        for element in elements:
            value = element.attrs["value"]
            if contain in value:
                return root_url + value

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

    def save_csv(*args):
        length = len(args[0])
        for arg in args:
            if len(arg) != length:
                return

        with open(file_path, 'a', encoding="utf-8") as file:
            writer = csv.writer(file,lineterminator="\n")
            for i in range(0, length):
                row = []
                for arg in args:
                    row.append(arg[i])
                writer.writerow(row)

    def get_urls():
        base_links = join(read_file(base_detail_links_file))
        # TODO
        # base_links = base_links[:length]
        urls = []
        for link in base_links:
            link_dic = {}
            link_dic["en"] = link
            for [key, value] in lang_conf.items():
                if value is None or len(value) == 0:
                    continue
                link_dic[key]=get_language_link(link, value)
            urls.append(link_dic)
        write_file(link_file, json.dumps(urls, indent=4, ensure_ascii=False))
        return urls

    with open(file_path, 'w', encoding="utf-8") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(lang_conf.keys())

    print("get_urls start")
    start=time.time()
    urls=get_urls()
    end=time.time()
    print(f'url time: {end - start}')
    print("get_urls end")

    for url in urls:
        args = []
        for lang in lang_conf.keys():
            args.append(crawler(url[lang]))
        save_csv(*args)
    return urls

# get_detail_links()
print("crawler_text start")
start=time.time()
crawler_text()
end=time.time()
print(f'time: {end - start}')
print("crawler_text end")
