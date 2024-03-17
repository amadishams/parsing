import requests
from bs4 import BeautifulSoup

url = "https://agroserver.ru/frukty-yagody/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

# response = requests.get(url,headers = headers)
# if response.status_code == 200:
#     with open("index14.html", "w", encoding="utf-8") as file:
#         file.write(response.text)
#         print("сохранено")
# else:
#     print("что то пошло не так")

with open("index14.html", "r", encoding="utf-8") as file:
    response = file.read()

soup = BeautifulSoup(response, "html5lib")
aaa = "https://agroserver.ru" + soup.find("ul", class_="pg").find_all("li")[-1].find("a")["href"]
number = int(soup.find("ul", class_="pg").find_all("li")[-1].find("a").text)

bbb = aaa.split("/")[0:-2]
vvv = "/".join(bbb)+"/"

for i in range(1, number+1):
    print(vvv + str(i))
