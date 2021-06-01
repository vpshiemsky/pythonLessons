"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1
Предприятия, с прибылью ниже среднего значения: Фирма_2
"""
from statistics import mean
from collections import defaultdict

COUNT = int(input("Введите количество предприятий для расчета прибыли:\n"))
dic_ = defaultdict(int)

for i in range(COUNT):
    company = input("Введите название предприятия:\n")
    profit = input("Введите через пробел введите прибыль данного "
                             "предприятия за каждый квартал "
                             "(всего 4 квартала):\n")
    dic_[company] = mean([int(el) for el in profit.split(" ")])

average = round(mean(dic_.values()),3 )

print(f"Средняя годовая прибыль всех предприятий: {average}.")
print(f"Предприятия, с прибылью выше среднего значения: "
      f"{', '.join([el for el in dic_.keys() if dic_[el] > average])}.")
print(f"Предприятия, с прибылью ниже среднего значения: "
      f"{', '.join([el for el in dic_.keys() if dic_[el] < average])}.")
