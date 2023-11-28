import requests
from bs4 import BeautifulSoup
import csv
import re
import json
import common

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
    def crawler(url):
        texts = []
        response = requests.get(url)
        text = response.text

        # Parse the HTML content
        soup = BeautifulSoup(text, "html.parser")
        for query in crawler_queries:
            elements = soup.select(query)
            extract_text(elements, texts)
        return texts

    base_links = join(read_file(base_detail_links_file))
    langs_1 =["newLanguage=vi", "newLanguage=en-"]
    langs_2 = ["vi", "en"]
    base_links=base_links[:1]
    for link in base_links:
        link_dic = {
            "vi": "",
            "en": "",
            "jp": link,
        }
        for i in range(0, len(langs_1)):
            url = get_language_link(link, langs_1[i])
            link_dic[langs_2[i]]=url
        print(link_dic)
crawler_text()
