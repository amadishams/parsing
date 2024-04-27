from moduls import *
from static_names import *


responce = get_page(url)
if responce:
    res = save_or_read_page(responce=responce,name_page=name_page,status="w", encode="cp1251")
    if res == None:
        responce = save_or_read_page(name_page=name_page, status="r", encode="cp1251")
else:
    print("Что-то пошло не так")

# soup = get_soup(responce, "html5lib")
# paginations = soup.find("div", class_="pager-items")
