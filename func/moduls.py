import requests
from bs4 import BeautifulSoup


def get_page(url):
    "Отправка запроса"
    responce = requests.get(url)
    if responce.status_code == 200:
        return responce.text
    return False
#
#
# def save_page(responce, name_page):
#     "сохраняет страницу сайта"
#     with open(name_page+".html", "w", encoding="utf-8") as file:
#         file.write(responce)
#         print("Страница сохранена")
#
#
# def read_page(name_page):
#     with open(name_page+".html","r", encoding="utf-8") as file:
#         return file.read()


def save_or_read_page(name_page,status,responce="", encode="utf-8"):
     with open(name_page + ".html", status, encoding=encode) as file:
         if responce:
            file.write(responce)
         return file.read()


# def get_soup(responce, pars="lxml"):
#     soup = BeautifulSoup(responce,pars)
#     return soup