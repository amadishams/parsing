import requests
from bs4 import BeautifulSoup

def get_response(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return False


def write_file(name, response, status="w", encod="utf-8"):
    with open(name, status, encoding=encod) as file:
        file.write(response)
        return "write"


def read_file(name, status="r", encod="utf-8"):
    with open(name, status,encoding=encod) as file:
        return file.read()

def write_read(name, status, encod="utf-8",response="" ):
    with open(name,status,encoding=encod) as file:
        if response:
            file.write(response)
            return "write"
        return file.read()


def pars_with_bs4(response):
    soup = BeautifulSoup(response,"html5lib")
    return soup


def get_pars_page(soup):
    x = soup.find("div", class_="pager-items").find_all("a")[-1]
    return x

