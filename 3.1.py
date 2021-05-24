"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""
#Сложность O(nlogn)+O(nlogn)+O(n)*O(1)*O(1)*O(1)*O(1)*O(1)*O(1)=O(2n log n)+O(n)
company={ 'Gord':100000,'MRKT':105000,'GUI':171000,'Tidal':192500,'Pyaterochka':164000}
sorted_values=sorted(company.values())                  #O(n log n)
sorted_keys=sorted(company.keys())                      #O(n log n)
result=[]
for i in range (3):                                     #O(n)
    max_values=max(sorted_values)                       # O(1)
    idx = sorted_values.index(max_sorted_values)        # O(1)
    rez.append(proceed[idx])                            # O(1)
    rez.append(company[idx])                            # O(1)
    sorted_keys.pop(idx)                                # O(1)
    sorted_values.pop(idx)                              # O(1)
print(result)

#Сложность O(2n^2)
companies={ 'Gord':100000,'MRKT':105000,'GUI':171000,'Tidal':192500,'Pyaterochka':164000}
company = [el for el in companies.keys()]                          #O(n)
proceed  = [el for el in companies.values()]                       #O(n)
rez = []
for i in range(3):                                                 #O(n)
    max_proceed = max(proceed)                                     #O(1)
    idx = proceed.index(max_proceed)                               #O(1)
    rez.append(proceed[idx])                                       #O(1)
    rez.append(company[idx])                                       #O(1)
    company.pop(idx)                                               #O(1)
    proceed.pop(idx)                                               #O(1)
print(rez)








