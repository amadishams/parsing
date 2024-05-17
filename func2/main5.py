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

def create_soup(ab,tag,clas):
    soup = BeautifulSoup(ab, "html5lib")
    bb = soup.find_all(tag,class_=clas)
    return bb


def generate_url(bb):
    url,number = bb[-1]["href"].split("=")
    return "https://www.alltime.ru" + url+"=", int(number)


def create_urls(url, number):
    for i in range(1, number):
        print(url+str(i))




# a = request(url)
# write(a)
b = read()
bb = create_soup(b,"a","pager-item pager-item--num")
ab,ac = generate_url(bb)
create_urls(ab,ac)