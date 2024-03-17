from bs4 import BeautifulSoup
# with open("index2.html",'r', encoding="UTF-8") as file:
#     aaaa = file.read()
# print(aaaa)

import requests

# url = "https://www.alltime.ru/watch/"
# aaa = requests.get(url)
# # print(aaa)
# if aaa.status_code == 200:
#
#     with open("index5.html", "w", encoding="cp1251") as file:
#         file.write(aaa.text)
#
# else:
# # print("Сайт недоступен")
#
with open("index5.html",'r', encoding="cp1251") as file:
     bbbb = file.read()
# print(bbbb)

soup = BeautifulSoup(bbbb,"html5lib")
# print(soup.find("div", class_="catalog-item-name text-h5").find("span").text)
card = soup.find_all("div", class_="catalog-item catalog-item--col4")
number_cards = len(card)

# for i in range(0,number_cards):
#     print(card[i].find("span").text)
# n = 0
# while True:
#     print(card[n].find("span").text)
#     n+=1
#     if n >= number_cards:
#         break

for car in card:
    try:
        print(car.find("span").text)
        print(car.find('span', class_='catalog-item-price text-h5').text.strip())
    except:
        pass
    
