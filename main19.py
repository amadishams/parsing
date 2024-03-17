
# n = ['1', '2']
# print(" ".join(n).split(" "))
#
# # print("Yunus").lower()
# n = input("Введите имя").lower()
# print(n)


url = "https://agroserver.ru/med-produkty-pchelovodstva/Y2l0eT18cmVnaW9uPXxjb3VudHJ5PXxtZXRrYT18c29ydD0xfGFjY2VwdF9nZT0x/4/"
url = url.split("/")
del url[-2]
url = '/'.join(url)
for i in range(1,11):
    print(url+str(i)+"/")

"""
1-убрать 4 с конца
2-добавить число от 1 до 10 вместо 4
"""

