salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
delta = spend - salary
money_capital = delta
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(2, months + 1):
    spend *= (1 + increase)
    delta = spend - salary
    money_capital += delta

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
