from abc import ABC

from bs4 import BeautifulSoup
import requests
import json
import os

class Crawler(ABC):
    @staticmethod
    def crawl(url):
        pass

class EaterCrawler(Crawler):
    @staticmethod
    def crawl(url):
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "lxml")

        meta = soup.find("script", {"type": "application/ld+json"}).text
        meta_dict = json.loads(meta)
        restaurants = {x["item"]["name"]: x["item"]["url"] for x in meta_dict["itemListElement"]}

        name_address_dict = {}

        for restaurant_name, url in restaurants.items():
            _, data_slug = os.path.split(url)
            name_address_dict[restaurant_name] = soup.find("section", {"data-slug": data_slug}).find("div", {"class": "c-mapstack__address"}).find("a").text

        return name_address_dict
