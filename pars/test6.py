from bs4 import BeautifulSoup
# with open("index2.html",'r', encoding="UTF-8") as file:
#     aaaa = file.read()
# print(aaaa)

import requests

url = "https://agroserver.ru/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

aaa = requests.get(url,     headers = headers)

if aaa.status_code == 200:

    with open("index6.html", "w", encoding="utf-8") as file:
        file.write(aaa.text)

else:
    print("Сайт недоступен")
