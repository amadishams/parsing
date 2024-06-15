import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint

url = "https://agroserver.ru/zerno/"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}
names=[]
prices=[]
def get_page():
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.text


def save_or_read(name, w_r, response=""):
    with open(name, w_r, encoding="utf-8") as file:
        if response:
            file.write(response)

        else:
            response = file.read()
            return response


def create_soup(response):
    soup = BeautifulSoup(response, "html5lib")
    return soup


def pas_url_end_number(soup):
    res = soup.find("ul", class_="pg_m").find_all("li")[-1].find("a")["href"].split("/")
    end_number = res[-2]
    del res[-2]
    res = "/".join(res)
    res_url = "https://agroserver.ru" + res
    return res_url,end_number


def all_urls(res_url, end_number):
    for number in range(1, int(end_number)+1):
        end_url = res_url + str(number)+"/"
        response = requests.get(end_url, headers=headers)
        yield response

def pause():
    n = randint(1,3)
    sleep(n)



    # if response.status_code == 200:
    #     with open("index.html", "w", encoding="utf-8") as file:
    #         file.write(response.text)
    # with open("index.html", "r", encoding="utf-8") as file:
    #     response = file.read()
    #
    # soup = BeautifulSoup(response, "html5lib")
    # cards = soup.find_all("div", class_="line")


    print(f"Парсинг страницы{number}/{end_number}")

def get_price(cards):
    names = []
    prices = []
    for card in cards:
        name_product = card.find("div", class_="th").text
        try:
            price = card.find("div", class_="price").text
        except:
            price = "not price"
        finally:
            # print(name_product)
            # print(price)
            names.append(name_product)
            prices.append(price)

def save_csv(names,prices):
    df = pd.DataFrame(
        {
            "Name": names,
            "Prices": prices
        }
    )
    df.to_csv("my_data.csv", mode="a", index=False, header=True)


def all_data_paginations(numbers, url):
    # for number in range(1, int(numbers + 1)):
    for number in range(1, 5):
        res_url = url + str(number)
        page = get_page(res_url)
        save_or_read(f"index{number}.html", "w", encod="cp1251", data=page)
        response = save_or_read(f"index{number}.html", "r", encod="cp1251")
        # soup = create_soup(response)
        # paginations = get_data(soup, "a", class_="pager-item pager-item--num")
        # page = get_page(res_url)
        # cards = get_cards(response)
        # get_price(cards)