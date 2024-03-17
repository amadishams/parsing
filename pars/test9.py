import requests
from bs4 import BeautifulSoup

# url = "https://www.velosklad.ru/velosipedy/type/podrostkovyie/"
# aaa = requests.get(url)
# if aaa.status_code == 200:
#     with open("index9.html", "w", encoding="utf-8") as file:
#         file.write(aaa.text)
# else:
#     print("Недоступен")

with open("index9.html","r", encoding="utf-8") as file:
    ab = file.read()

soup = BeautifulSoup(ab, "html5lib")
aaaa = soup.find_all("div", class_="ah-products-item__line")
# print(aaaa)
for i in aaaa:
    print(i.find('a').text)
