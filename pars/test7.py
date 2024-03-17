from bs4 import BeautifulSoup

import requests

# url = "https://www.alltime.ru/watch/"
# aaa = requests.get(url)
#
# if aaa.status_code == 200:
#     with open("index7.html", "w", encoding="cp1251") as file:
#         file.write(aaa.text)
# else:
#     print("Что-то пошло не так")

with open("index7.html", "r", encoding="cp1251") as file:
    b = file.read()
# print(b)

soup = BeautifulSoup(b,"html5lib")
name = soup.find_all("div", class_='catalog-item--col4')
# print(name)
for i in name:
    print(i.find("span").text)

