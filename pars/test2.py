from bs4 import BeautifulSoup
from pprint import pprint

with open("index2.html", "r", encoding="utf=8") as file:
    aaa = file.read()

soup = BeautifulSoup(aaa,"lxml")
x = (soup.find_all("div")[1:])
x = x[:-1]
for i in x:
    print(i.find("p").text)

pprint(soup.find_all("a")[1]["href"])
pprint(soup.find("div",class_='k').text)
