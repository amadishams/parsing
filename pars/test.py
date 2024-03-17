import requests
from bs4 import BeautifulSoup

with open("index2.html", "r", encoding="utf=8") as file:
    xxx = file.read()

soup = BeautifulSoup(xxx, "lxml")
# print(soup.find_all("div")[0].find('p').text)
# print(soup.find_all("div")[1].find('p').text)
# print(soup.find_all("div")[2].find('p').text)
# print(soup.find_all("div")[3].find('p').text)

# data = soup.find_all("div")
# data = data[:-1]
# for i in data:
#     print(i.text)

print("https://www.alltime.ru/"+soup.find("div").find("a")["href"])
# print(soup.find("div", class_="k").text)
# print(soup.find("a")["href"])