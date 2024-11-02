name = "Sasha"
position = "junior"
experience = 0
base_salary = 11500
tax = 0

# Перевірка валідності вхідних даних
if base_salary < 0 or experience < 0:
    print(f"Помилка: некоректні дані для {name}.")
else:
    # Визначаємо ставку податку
    if base_salary < 10000:
        tax = 10
    elif base_salary <= 20000:
        tax = 15
    else:
        tax = 18

    # Визначаємо ставку бонусу
    bonus = 0
    if position == "junior" and experience > 1:
        bonus = 5
    elif position == "middle" and experience >= 3:
        bonus = 10
    elif position == "senior" and experience >= 5:
        bonus = 15

    # Розрахунок зарплати після податків і бонусів
    tax_money = base_salary / 100 * tax
    salary_after_tax = base_salary - tax_money
    bonus_money = salary_after_tax * (bonus / 100)
    final_salary = salary_after_tax + bonus_money

    print(f"{name}, ваша кінцева зарплата після податків і бонусів: {final_salary}.")
