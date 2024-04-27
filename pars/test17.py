import requests
from bs4 import BeautifulSoup

url = "https://www.audible.com/adblbestsellers?searchCategory=18571910011&ref_pageloadid=not_applicable&ref=a_adblbests_l1_catRefs_1&pf_rd_p=2ea8d46b-3372-49db-8ad4-77416e49695f&pf_rd_r=RPDCGG67X0KREMA5GWAF&pageLoadId=hDd0KJOOeZH7fjs8&creativeId=00b943e2-39f7-4416-aa6b-3c2695ade879"
responce = requests.get(url).text
# if responce.status_code == 200:
#     with open("index17.html", "w", encoding="utf-8") as file:
#         file.write(responce.text)
#         print("ok")
# else:
#     print("Что то пошло не так")
#
with open("index17.html", "r", encoding="utf-8") as file:
    response = file.read()

soup = BeautifulSoup(responce, "html5lib")
aaa = soup.find("li", class_="productListItem")
print(aaa)



