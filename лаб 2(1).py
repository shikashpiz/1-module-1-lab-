money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05 # Ежемесячный рост цен
mes = 0


cap_mes = money_capital
while cap_mes + salary > spend:
    mes += 1
    cap_mes += salary
    cap_mes -= spend
    spend *= (1 + increase)





# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", mes)
