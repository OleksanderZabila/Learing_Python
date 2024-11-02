bill = float(input("Введіть суму рахунку: "))
payment_method = input("Введіть спосіб оплати (готівка або картка): ").lower()
loss = 0
money = bill  # Встановлюємо значення money дорівнює bill за замовчуванням

if bill > 500 and payment_method == "готівка":
    loss = bill / 100 * 10
    money = bill - loss
    print(f"Знижка складає: {loss} грн. До сплати: {money} грн.")
elif bill > 500 and payment_method == "карта":
    loss = bill / 100 * 5
    money = bill - loss
    print(f"Знижка складає: {loss} грн. До сплати: {money} грн.")
else:
    print(f"Знижка складає: {loss} грн. До сплати: {money} грн.")
