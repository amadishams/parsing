import time
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from random import randint

url = "https://www.alltime.ru/watch/"

# responce = requests.get(url)
# if responce.status_code == 200:
#     with open("index12.html", "w", encoding="cp1251") as file:
#         file.write(responce.text)
#         print("Успех")
# else:
#     print("нет доступа")

with open("index12.html", "r", encoding="cp1251") as file:
     responce = file.read()

soup = BeautifulSoup(responce, "html5lib")
cards = soup.find_all("div", class_="catalog-item catalog-item--col4")
paginations = soup.find("div", class_="pager-items").find_all("a", class_="pager-item pager-item--num")[1]["href"]
end_number_page = int(soup.find("div", class_="pager-items").find_all("a", class_="pager-item pager-item--num")[-1].text)
res_url = "https://www.alltime.ru" + paginations.split("=")[0]+"="

for page in range(1, end_number_page+1):
    responce = requests.get(res_url+str(page))

    # with open(f"./html_files/index{page}.html", "w", encoding="cp1251") as file:
    #     file.write(responce.text)
    # print(f"done page save {page}/{end_number_page}")

    with open(f"html_files/index{page}.html", "r", encoding="cp1251") as file:
        responce = file.read()

    soup2 = BeautifulSoup(responce, "html5lib")
    cards = soup2.find_all("div", "catalog-item catalog-item--col4")


    for card in cards:

        try:
            print(card.find("span").text)
            print(card.find("span", class_="catalog-item-price text-h5").text.strip())
        except:
            pass



