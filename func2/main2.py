import requests
from bs4 import BeautifulSoup
from pprint import pprint

def get_req(url):
    info = requests.get(url)
    print(info.status_code)
    if info.status_code == 200:
        return info.text

def write(info):
    with open("index.html","w",encoding="cp1251") as file:
        file.write(info)

def read():
    with open("index.html", "r", encoding="cp1251") as file:
        x = file.read()
        return x


def write_read(text="", status="r",file_number=0):
    with open(f"index{file_number}.html", status, encoding="cp1251") as file:
        if text:
            file.write(text)
        else:
            x = file.read()
            return x


def soup_file(x,tag,clas_=""):
    soup = BeautifulSoup(x, 'html5lib')
    a = soup.find_all(tag,class_=clas_)
    return a


def get_end_number_and_url(list):
    url, number = list[-1]["href"].split("=")
    return "https://www.alltime.ru"+url+"=", int(number)


def create_urls_paginations(result_url, end_number):
    for i in range(1, end_number+1):
        yield result_url + str(i)


def save_all_pages(url, end_number):
    for i in range(1,5):
        text = get_req(url)
        print(text)
        # write_read(text,"w", file_number=i)


# text = get_req(url="https://www.alltime.ru/watch/")
# write_read(text,"w")
response = write_read()
pages = soup_file(response,"a","pager-item pager-item--num")
res_url, end_number = get_end_number_and_url(pages)
url = create_urls_paginations(res_url,end_number)
save_all_pages(next(url),end_number)