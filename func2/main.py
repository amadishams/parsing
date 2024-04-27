from static_names import *
from moduls import *

# response = get_response(url)
# if response:
#     w = write_read(name_file,"w","cp1251",response)
# else:
#     w = False
#     print("Нет доступа к сайту")

# if w == "write":
response = write_read(name_file,"r","cp1251")

print("успех")


soup = pars_with_bs4(response)
paginations = get_pars_page(soup)
print(paginations["href"].split("=")[0]+"=")
print(paginations["href"].split("=")[1]+"=")
