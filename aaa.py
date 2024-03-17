db = {}

while fam := "0":
    fam = input("Введите фамилию участника").lower()
    proizv = input("Введите название произведения").lower()
    db[proizv] = [fam]
    print(db)





    # if ans in books:
    #     info = books[ans]
    #     print("Ряд", info[0])
    #     print("Полка", info[1])