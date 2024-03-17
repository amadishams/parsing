import requests
from bs4 import BeautifulSoup
import time, random
url = "https://www.backcountry.com/mountain-bikes"

responce = requests.get(url).text


soup = BeautifulSoup(responce, "html5lib")
aaa,end_number = soup.find_all("a", class_="chakra-link css-1i3ypl1")[-1]["href"].split("=")
aaa = "https://www.backcountry.com" + aaa + "="

for i in range(1,int(end_number)+1):
# for i in range(1,2):
    page = aaa + str(i)
    page_responce = requests.get(page).text

    soup = BeautifulSoup(page_responce,"html5lib")
    name = soup.find_all("div", class_="css-fmt7bd")
    for a in name:
        print(a.find("p", class_="chakra-text css-nxn9mj").text)
        print(a.find("h2", class_="chakra-heading css-1gfqank").text)
        print(a.find("span", class_="chakra-text css-10mpi4h").text.split("Original")[0])
    print(f"Обработка страниц {i}/{end_number}")
    x = random.randint(1,4)
    time.sleep(x)

