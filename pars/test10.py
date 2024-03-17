import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://www.alltime.ru/watch/"

# aaa = requests.get(url)
# if aaa.status_code == 200:
#     with open("index10.html", "w", encoding="utf-8") as file:
#         file.write(aaa.text)
#         print("Успех")
# else:
#     print("нет доступа")

with open("index10.html", "r", encoding="utf-8") as file:
    ab = file.read()

soup = BeautifulSoup(ab, "html5lib")
ssss = soup.find_all("div", class_="catalog-item catalog-item--col4")
# print(ssss)
paginations = soup.find("div", class_="pager-items").find_all("a")
end_number = int(soup.find("div", class_="pager-items").find_all("a",class_="pager-item--num")[-1].text)
print(end_number)

result_url = "https://www.alltime.ru/" + paginations[1]["href"]
result_url = result_url.split("=")[0]+"="

for i in range(1,end_number+1)
    print(result_url+str(i))


# for i in ssss:
#     try:
#         name = i.find("span").text
#         if name:
#             print("Название:", name)
#         else:
#             print("Название","Реклама")
#     except Exception as ex:
#         print(ex)
#         print("Название", "реклама")
#     try:
#         print("Старая цена",i.find("span", class_="catalog-item-price_old text-h5").text)
#     except Exception as ex:
#         print("Старой цены нет")
#     try:
#         print("Новая цена",i.find("span", class_="catalog-item-price text-h5").text.strip())
#     except:
#         print("Новой цены нет")
#     finally:
#         print("*" * 10)
