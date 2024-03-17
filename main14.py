str
x = "amadi"
int
x = 1
bool
x = 1 > 0
tuple
x = (1,2,3)
set
x = {'amadi','yunus'}

list
x = [1,2,3]
dict
x = {"amadi": "python"}
float
x = 1.5
print(type(x))

# list - это упорядоченный, изменяемый тип данных


books = {
    'book1': [1,2],
    'book2': [2,3]
}

while True:
    a = input('?')
    if a in books:
        print(books[a][1])
    else:
        b = input('Книга не найдена,добавить?')
        if b == 'да':
            r = input('добавить ряд')
            p = input('добавить полку')
            books[a]=[r,p]
        print(books)


while True:
    print('hello')



for a in 'amadi':
    print(a)