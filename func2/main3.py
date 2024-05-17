from main2 import *

write(get_req("https://www.alltime.ru/watch/"))
page = soup_file(read(),"a","pager-item pager-item--num")
pprint(page)