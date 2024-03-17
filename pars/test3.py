import requests

url = "https://www.alltime.ru/watch/"

# response = requests.get(url)
# if response.status_code == 200:
#     print("Есть доступ!!!")
#
#     with open("index3.html", "w", encoding="cp1251") as file:
#         file.write(response.text)

with open("index3.html", 'r', encoding="cp1251") as file:
    responce = file.read()
print(responce)