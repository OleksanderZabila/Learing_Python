age = 21

if age < 0:
    print ("error")
else:
    if age < 13:
        print ("Дитина")
    elif age > 13 and age <= 19:
        print("Підліток")
    elif age >= 20 and age <= 64:
        print("Дорослий")
    else:
        print("Пенсіонер")

