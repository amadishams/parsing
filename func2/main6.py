import requests
from bs4 import BeautifulSoup

url = "https://www.alltime.ru/watch/"
def request(url):
    a = requests.get(url)
    # print(a)
    if a.status_code == 200:
        return a.text


def write(a):
    # print(a)
    with open("index.html", "w", encoding="cp1251") as file:
        file.write(a)

def read():
    with open("index.html", "r", encoding="cp1251") as file:
            return file.read()

def create_soup(text,tag,clas):
    soup = BeautifulSoup(text,"html5lib")
    aa = soup.find_all(tag,class_=clas)
    return aa


def create_url(aa):
    url,number = aa[-1]["href"].split("=")
    return "https://www.alltime.ru"+url+"=",int(number)


def generate_urls(url,number):
    for i in range(1,number):
        print(url+str(i))


# a = request(url)
# write(a)
b = read()
aa = create_soup(b,"a", "pager-item pager-item--num")
url,number = create_url(aa)
generate_urls(url,number)