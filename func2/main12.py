import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.alltime.ru/watch/"

def get_page(url):
    responce = requests.get(url)
    if responce.status_code == 200:
        return responce.text

def save_read(name, w_r,response=""):
    with open(name, w_r, encoding="utf-8") as file:
        if response:
            file.write(response)
        else:
            response = file.read()
            return response

def create_soup(response):
    soup = BeautifulSoup(response,"html5lib")
    return soup


def all_cards(soup):
    cards = soup.find_all("div", class_="catalog-item-content")
    return cards


def one_card(cards):
    titles=[]
    prices=[]
    for card in cards:
        try:
            title = card.find("div", class_="catalog-item-name text-h5").find("span").text
            price = card.find("span", class_="catalog-item-price text-h5").text.strip()
        except:
            title = "нет товара"
            price = "нет цены"
        finally:
            titles.append(title)
            prices.append(price)

    return titles,prices

def save_csv(titles, prices):
    df = pd.DataFrame(
        {
            "Name": titles,
            "Price": prices

        }
    )
    df.to_csv("my_data2.csv", mode="w", index=False, header=True)


def all_paginations(response):
    res_url, end_number = response.find_all("a", class_="pager-item pager-item--num")[-1]["href"].split("=")
    return "https://www.alltime.ru"+res_url+"=", int(end_number)


def create_urls(res_url,end_number):
    for i in range(1, end_number+1):
        result_urls = (res_url+str(i))
        yield result_urls


def get_all_pages(result_urls, end_number):
    for i in range(1, end_number+1):
        page = get_page(result_urls)
        soup = create_soup(page)
        cards = all_cards(soup)
        titles, prices = one_card(cards)
        print(titles)
        print(prices)


# response = get_page(url)
# save_read("index.html", "w", response)
response = save_read("index.html", "r")
soup = create_soup(response)
cards = all_cards(soup)
titles, prices = one_card(cards)
save_csv(titles,prices)
res_url, end_number = all_paginations(soup)
result_urls = create_urls(res_url,end_number)
get_all_pages(next(result_urls),end_number)