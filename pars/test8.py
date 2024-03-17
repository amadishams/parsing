import requests
from bs4 import BeautifulSoup

# url = "https://agroserver.ru/zerno/"
# headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
# response = requests.get(url,headers = headers)
# if response.status_code == 200:
#     print("успех")
#     with open("index8.html", "w", encoding="utf-8") as file:
#         file.write(response.text)
# else:
#     print("Доступ запрещен")

with open("index8.html", "r", encoding="utf-8") as file:
    bb = file.read()

soup = BeautifulSoup(bb, "html5lib")
ab = soup.find_all("div", class_="tovar_top")
print(ab)

for i in ab:
    try:
        print(i.find("div", class_="th").find('a').text)
        print(i.find("div", class_="price").text.split('/')[0])
    except:
        pass
