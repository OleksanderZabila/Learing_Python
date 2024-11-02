# розробити систему для реєстрації подій і збору інформації про відвідувачів.
# Твоє завдання — визначити вік учасника, перевірити, чи він відповідає віковим вимогам для участі,
# та додати його до списку учасників, якщо він підходить.
full_name = "Забіла Олександр"
birth_year = 2003
current_year = 2024
min_age = 18

calculated_age = current_year - birth_year

if calculated_age >= 100:
    print(f"Помилка : неправильно вказаний рік народження для {full_name}.")
elif calculated_age >= min_age:
    print(f"{full_name} допущено до участі. Вік: {current_year}.")
else:
    print(f"{full_name} не відповідає віковим вимогам. Вік: {current_year}")
