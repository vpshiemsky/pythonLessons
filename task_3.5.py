"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача:
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.
Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""
from collections import deque
from timeit import timeit
from random import randint


lst1 = []
deque1 = deque()
lst2 = [i for i in range(10 ** 5)]
n = 10 ** 4
some_deque2 = deque([i for i in range(10 ** 5)])



def fill_deque(dq):
    for i in range(n):
        dq.appendleft(i)
    return dq

def fill_list(lst):
    for i in range(n):
        lst.insert(0, i)
    return lst

def changer_deque(dq):
    for _ in range(90000):
        dq[randint(1, 8001)] = randint(1, 150)
    return dq

if __name__ == '__main__':
    print('Время заполнения списка при 12 повторениях: ', timeit(
        'fill_list(lst1)',
        setup='from __main__ import fill_list, lst1, n',
        number=12))
if __name__ == '__main__':
    print('Время заполенения дека при 12 повторениях : ',
        timeit('fill_deque(deque1)',
        setup='from __main__ import fill_deque , deque1, n',
        number =12))