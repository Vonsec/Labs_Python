import math

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

money_capital = math.ceil(
    math.fsum(
        max(0, spend * math.pow(1 + increase, month) - salary)
        for month in range(months)
    )
)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
