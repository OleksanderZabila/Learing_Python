number = int(input("Введіть число: "))
rezult = ""
for i in range(1,number + 1):
    if i % 2 == 0:
        rezult += str(i)+", "

if rezult:
    print(f"Парні числа від 1 до", number, ":", rezult[:-2])
else:
    print("Парних чисел немає.")