import time
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from random import randint

url = "https://www.alltime.ru/watch/"


def get_page(url):
    responce = requests.get(url)
    if responce.status_code == 200:
        return responce.text
    return False


def save_page(responce, page =1):
    with open(f"index{page}.html", "w", encoding="cp1251") as file:
        file.write(responce)

def file_read(page =1):
    with open(f"index{page}.html", "r", encoding="cp1251") as file:
        responce = file.read()
    return responce


def soup_file(response, tag="div", clas="catalog-item catalog-item--col4"):
    soup = BeautifulSoup(response, 'html5lib')
    cards = soup.find_all(tag, class_=clas)
    return cards,soup


def get_url_number(soup):
    paginations = soup.find("div", class_="pager-items").find_all("a", class_="pager-item pager-item--num")[1]["href"]
    end_number_page = int(soup.find("div", class_="pager-items").find_all("a", class_="pager-item pager-item--num")[-1].text)
    res_url = "https://www.alltime.ru" + paginations.split("=")[0]+"="
    return end_number_page,res_url


def result_url_get_data(end_number_page,res_url):
    # for page in range(1, end_number_page+1):
    for page in range(1, 5):
        responce = requests.get(res_url+str(page))
        save_page(responce, page)
        print(f"done page save {page}/{end_number_page}")


def get_cards_data(response):
    cards, soup = soup_file(response, clas="catalog-item catalog-item--col4")
    for card in cards:

        try:
            print(card.find("span").text)
            print(card.find("span", class_="catalog-item-price text-h5").text.strip())
        except:
            pass

def read_pages(end_number_page):
    # for page in range(1, end_number_page +1):
    for page in range(1, 5):
        response = file_read(page)
        get_cards_data(response)



x = get_page(url)
if x:
    save_page(x)
    response = file_read()

    cards, soup = soup_file(response)
    end_number, res_url = get_url_number(soup)
    result_url_get_data(end_number,res_url)
    read_pages(end_number)





