salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
save = 0
spend1 = 0
salary1 = 0
for i in range (1,(months + 1)):
    salary1 += salary
    spend1 += spend
    spend *= (1 + increase)
save = spend1 - salary1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(save))
