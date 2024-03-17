import requests

url = "https://www.bestwatch.ru/watch/filter/pol:mens/"

# responce = requests.get(url)
# if responce.status_code == 200:
#     print("Есть доступ")
#
#     with open("index4.html", 'w', encoding="UTF-8") as file:
#         file.write(responce.text)

with open("index4.html", 'r', encoding="UTF-8") as file:
    responce = file.read()
print(responce)