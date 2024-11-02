number = int(input("Введіть число для таблиці множення: "))
temp = 0
sum = 0
#while temp <= 10:
#    print(f"{number} * {temp} = {sum} ")
#     temp += 1
#        sum = temp * number
for temp in range (10):
    print(f"{number} * {temp} = {sum} ")
    sum = temp * number

