import requests
from bs4 import BeautifulSoup

url = "https://megamarket.ru/catalog/velosipedy/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br, zstd",
    "Accept-Language":"ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"




           }

responce = requests.get(url, headers = headers)
if responce.status_code == 200:
    with open("index15.html", "w", encoding="utf-8") as file:
        file.write(responce.text)
        print("ok")
else:
    print("Что то пошло не так")

with open("index15.html", "r", encoding="utf-8") as file:
    response = file.read()
print(response)
# soup = BeautifulSoup(response,"html5lib")
# aaa = soup.find("nav", class_="catalog-items-list__pager")
# print(aaa)
