number = int(input("Введіть число: "))
temp = number
temp1 = 0
#for number in range(number):
#    temp1 += 1
#    temp = temp1 + temp
while temp1 != number:
    temp1 += 1
    temp = temp1 + temp
print(f"Сума чисел від 1 до {number} = {temp}")