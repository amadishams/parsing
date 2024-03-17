import time
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from random import randint


url = "https://agroserver.ru/zerno/"

# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
# responce = requests.get(url,headers = headers)
# if responce.status_code == 200:
#     with open("index13.html", "w", encoding="utf-8") as file:
#         file.write(responce.text)
#         print("Успех")
# else:
#     print("нет доступа")

with open("index13.html", "r", encoding="utf-8") as file:
    responce = file.read()

soup = BeautifulSoup(responce, "html5lib")
cards = soup.find_all("div", class_="tovar_top")
paginations = soup.find("ul", class_="pg").find_all("li")[1].find("a")["href"]
aa = paginations.split("/")
del aa[-2]
aa = "/".join(aa)
end_number_page = int(soup.find("ul", class_="pg").find_all("li")[-1].text)
res_url = "https://agroserver.ru" + aa
print(res_url)
for page in range(1, end_number_page+1):
    print(res_url+str(page)+"/")

