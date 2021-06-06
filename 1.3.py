"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
from time import time

list_ = []
dict_ = {}
n = 10 ** 5


def first_decorator(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Время выполенения функции {func.__name__} '
              f'составило {end - start}')
        return result

    return timer

@first_decorator
def fill_list_insert(lst, num):
    for i in range(num):
        lst.insert(0, i)

fill_list_insert(list_, n)
print('_' * 100)


@first_decorator
def fill_list_append(lst, num):
    for i in range(num):
        lst.append(i)


fill_list_append(list_, n)
print('_' * 100)


@first_decorator
def fill_dict(dct, num):
    for i in range(num):
        dct[i] = i


fill_dict(dict_, n)
print('_' * 100)

