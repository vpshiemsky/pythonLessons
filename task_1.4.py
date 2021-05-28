"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""
import timeit
from timeit import Timer


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_arr = [i for i in enumerate(nums) if nums[i] % 2 ==0 ]
    return new_arr


NUMBER=[el for el in range(1000)]

print(
    timeit.timeit(
        "func_1(NUMBER)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_2(NUMBERS)",
        globals=globals(),
        number=1000))

