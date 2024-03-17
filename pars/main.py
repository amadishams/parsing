import requests
from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf=8") as file:
    xxx = file.read()
print(xxx)

soup = BeautifulSoup(xxx, "lxml")
print(soup.find_all('p')[1].text)
print(soup.find("div").find("p").text)