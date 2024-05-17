import requests
from bs4 import BeautifulSoup

url = "https://agroserver.ru/zapchasti/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

def request(url,headers):
    ans = requests.get(url,headers=headers)
    if ans.status_code == 200:
        return ans.text

def save(ans):
    with open("index1.html","w",encoding="utf-8") as file:
        file.write(ans)


def read():
    with open("index1.html", "r", encoding="utf-8") as file:
        a = file.read()
        return a


def soup_file(x,tag,clas_=""):
    soup = BeautifulSoup(x, 'html5lib')
    a = soup.find_all(tag,class_=clas_)
    return a