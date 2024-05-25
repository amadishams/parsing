import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_page(url):
    status = requests.get(url)
    if status.status_code == 200:
        return status.text
    return False


def save_read_file(name, w_r, data=False):
    with open(name, w_r, encoding="cp1251") as file:
        if data:
            file.write(data)
        else:
            return file.read()


def create_soup(data):
    soup = BeautifulSoup(data,"html5lib")
    return soup


def get_all_tag(soup, tag, class_):
    pages, number = soup.find_all(tag, class_=class_)[-1]["href"].split("=")
    return "https://www.alltime.ru"+pages+"=", int(number)


def create_urls(page_url, number):
    # for page in range(1, number + 1):
    for i in range(1,5):
        response = get_page(page_url)
        save_read_file(data = response,w_r="w", name=f"files/index{i}.html")
        result_response = save_read_file(w_r="r", name=f"files/index{i}.html")
        print(f"save page {i}/{number}...")
        cards = get_cards(result_response)
        get_data_result(cards)

def get_cards(result_response):
    soup = create_soup(result_response)
    cards = soup.find_all("div", class_="catalog-item catalog-item--col4")
    return cards


def get_data_result(cards):
    for card in cards:
        title = card.find("div", "catalog-item-name text-h5").text.strip()
        # price = card.find("span", class_="catalog-item-price text-h5").text
        print(title)
        # print(price)

# response = get_page(url = "https://www.alltime.ru/watch/")
# save_read_file(data=response,name="index.html", w_r="w")
data = save_read_file(name="index.html", w_r="r")
soup = create_soup(data)
page_url, number = get_all_tag(soup=soup, tag="a", class_="pager-item pager-item--num")
create_urls(page_url=page_url, number=number)