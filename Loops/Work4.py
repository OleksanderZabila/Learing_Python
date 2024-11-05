start = int(input("Введіть початкове число:"))
end = int(input("Введіть кінцеве число:"))
rezult = ""

for i in range(start, end+1):
    if (i % 3 == 0 or i % 5 == 0) and not (i % 15 == 0):
        rezult += str(i) + ", "

if rezult:
    print(f"Числа, які діляться на 3 або 5, але не на обидва: {rezult[:-2]}")
else:
    print("Парних чисел немає.")