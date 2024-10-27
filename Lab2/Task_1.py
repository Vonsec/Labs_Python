from itertools import accumulate, count, islice

money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

expenses = (spend * (1 + increase) ** month for month in count(0))
balance_generator = accumulate((salary - expense for expense in expenses), initial=money_capital)
months = next(i for i, balance in enumerate(islice(balance_generator, 1, None)) if balance < 0)

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", months)
