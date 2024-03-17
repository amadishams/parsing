import time
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from random import randint

url = "https://www.alltime.ru/watch/"

# aaa = requests.get(url)
# if aaa.status_code == 200:
#     with open("index11.html", "w", encoding="cp1251") as file:
#         file.write(aaa.text)
#         print("Успех")
# else:
#     print("нет доступа")

with open("index11.html", "r", encoding="cp1251") as file:
    ab = file.read()

soup = BeautifulSoup(ab, "html5lib")
paginations = "https://www.alltime.ru" +soup.find('div',class_="pager-items").find_all("a")[-1]["href"]
url_page, end_number = paginations.split("=")
print(url_page)
print(end_number)
for number_page in range(1, int(end_number)+1):
    x = randint(1,2)
    result_url = url_page+"="+str(number_page)
    responce = requests.get(result_url)
    with open(f"./html_files/index{number_page}.html", "w", encoding="cp1251") as file:
        file.write(responce.text)
    time.sleep(x)
    print(f"Страница номер: {number_page}/{end_number}")

    with open(f"html_files/index{number_page}.html", "r", encoding="cp1251") as file:
        responce = file.read()
    soup2 = BeautifulSoup(responce,"html5lib")
    cards = soup2.find_all("div", "catalog-item catalog-item--col4")

    for i in cards:
        try:
            print(i.find("span").text)
            print(i.fin("span", class_="catalog-item-price text-h5").text.strip())
        except:
            pass
