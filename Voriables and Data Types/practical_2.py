#Ти створюєш систему для реєстрації в спортклубі, яка обирає абонемент залежно від віку та статусу студента.
name =  "Sasha"
age = 21
is_student = True
student = "студентческий"
kid = "дитячий"
adult = "стандартний"
if age > 100:
    print(f"Помилка : некоректний вік для {name}.")
elif age >= 18 and age <= 25 and is_student == True:
    print(f"{name}, ваш абонимент: {student}")
elif age > 25:
    print(f"{name}, ваш абонимент: {adult}")
elif age > 0 and age < 18:
    print(f"{name}, ваш абонимент: {kid}")
else:
    print("ERROR")