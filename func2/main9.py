import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.alltime.ru/watch/"


def get_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text


def save_read(name, w_r, encod,data=""):
    with open(name, w_r, encoding=encod)as file:
        if data:
            file.write(data)
        else:
            response = file.read()
            return response


def create_soup(response):
    soup = BeautifulSoup(response, "html5lib")
    return soup


def get_data(soup, tag, class_):
    paginations = soup.find_all(tag, class_=class_)
    return paginations


def pars_url(paginations):
    res_url,end_number = paginations[-1]["href"].split("=")
    # print(res_url)
    # print(end_number)
    return "https://www.alltime.ru"+res_url+"=", end_number


def get_cards(data):
    'возвращает кажду карточку'
    soup = create_soup(data)
    cards = get_data(soup,"div","catalog-item-content")
    return cards


def get_title_price(cards):
    titles = []
    prices = []
    for card in cards:
        title = card.find("span").text
        titles.append(title)
        try:
            price = card.find("span",class_="catalog-item-price text-h5").text.strip()
        except:
            price = "not price"
        finally:
            prices.append(price)
    save_csv(titles,prices)



def save_csv(names,prices):
    df = pd.DataFrame(
        {
            "Name": names,
            "Price": prices
        }
    )
    # print(df)
    df.to_csv("my_data.csv",mode="a",index=False, header=True)


def all_data_paginations(numbers, url):
    # for number in range(1, int(numbers + 1)):
    for number in range(1, 3):
        res_url = url + str(number)
        page = get_page(res_url)
        save_read(f"index{number}.html", "w", encod="cp1251", data=page)
        response = save_read(f"index{number}.html", "r", encod="cp1251")
        # soup = create_soup(response)
        # paginations = get_data(soup, "a", class_="pager-item pager-item--num")
        # page = get_page(res_url)
        cards = get_cards(response)
        get_title_price(cards)

# response = get_page(url)
# save_read("index.html", "w", encod="cp1251", data=response)
response = save_read("index.html","r", encod="cp1251")
soup = create_soup(response)
paginations = get_data(soup,"a", class_="pager-item pager-item--num")
res_url, end_number = pars_url(paginations)
all_data_paginations(url=res_url, numbers=end_number)
# cards = get_cards(response)
# get_title_price(cards)