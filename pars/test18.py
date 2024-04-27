import requests
from bs4 import BeautifulSoup

url = "https://agroserver.ru/med-produkty-pchelovodstva/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}


responce = requests.get(url, headers = headers )

if responce.status_code == 200:
    with open("index18.html", "w", encoding="utf-8") as file:
        file.write(responce.text)
        print("ok")
else:
    print("Что то пошло не так")

# with open("index18.html", "r", encoding="utf-8") as file:
#     responce = file.read()
#
# soup = BeautifulSoup(responce, "html5lib")
# aaa = soup.find_all("div", class_="tovar_top")
# print(aaa)


