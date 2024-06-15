import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint

url = "https://agroserver.ru/zerno/"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}


# response = requests.get(url=url, headers=headers)
# print(response.status_code)
# if response.status_code == 200:
#     with open("index.html", "w", encoding="utf-8") as file:
#         file.write(response.text)

with open("index.html", "r", encoding="utf-8") as file:
    response = file.read()

soup = BeautifulSoup(response, "html5lib")

res = soup.find("ul", class_="pg_m").find_all("li")[-1].find("a")["href"].split("/")
end_number = res[-2]
del res[-2]
res = "/".join(res)
res_url = "https://agroserver.ru" + res

for number in range(1, int(end_number)+1):
    end_url = res_url + str(number)+"/"
    response = requests.get(end_url, headers=headers)

    n = randint(1,3)
    sleep(n)

    if response.status_code == 200:
        with open("index.html", "w", encoding="utf-8") as file:
            file.write(response.text)
    with open("index.html", "r", encoding="utf-8") as file:
        response = file.read()

    soup = BeautifulSoup(response, "html5lib")
    cards = soup.find_all("div", class_="line")
    names:[]
    prices:[]

    print(f"Парсинг страницы{number}/{end_number}")

    for card in cards:
        name_product = card.find("div", class_="th").text
        try:
            price = card.find("div", class_="price").text
        except:
            price = "not price"
        finally:
            # print(name_product)
            # print(price)
            names.append(name_product)
            prices.append(price)

        df = pd.DataFrame(
            {
                "Name": names,
                "Prices": prices
            }
        )
        df.to_csv("my_data.csv", mode="a", index=False, header=True)