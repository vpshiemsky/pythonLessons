"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым из них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""

import time
from collections import OrderedDict
dict_={}
ordered_dict_=OrderedDict()
n=10 ** 5

def time_decor(func):
    def wrapper(*args , **kwargs):
        start = time.time()
        result = func(*args , **kwargs)
        end = time.time()
        print(f'Время выполениня функции {func.__name__} : '
              f'{end - start}')
        return result
    return wrapper

@time_decor
def fill_dict(dct,numb):
    for i in range(numb):
        dct[i] = i

@time_decor
def fill_ordered_dict(dct, numb):
    for i in range(numb):
        ordered_dict_[i] = i

fill_dict(dict_ , n)
fill_ordered_dict(ordered_dict_, n)

