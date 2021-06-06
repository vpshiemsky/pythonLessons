"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.
Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from memory_profiler import profile
import time
import timeit


def decor(func):
    def wrapper(*args , **kwargs):
        start = time.time()
        result = func(*args , **kwargs)
        end = time.time()
        print(f'Время выполнения функции {func.__name__}'
              f' заняло {end - start} секунд')
        return result

    return wrapper()
#Есть проблема , в принте он выводит название функции wrapper ,
# подскажите , что не так?
#1
@decor
@profile
def task_1_1():
    x=[i for i in range(10000)]
    return x

print('Время выполнения timeit составило ',
    timeit.timeit(
        "task_1_1",
        globals=globals(),
        number=10000) ,' секунд')
#Единственное, не понимаю , почему в timeit выполняется быстрее,можете подсказать?
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    32     19.5 MiB     19.5 MiB           1   @decor
    33                                         @profile
    34                                         def task_1_1():
    35     19.8 MiB      0.3 MiB       10003       x=[i for i in range(10000)]
    36     19.8 MiB      0.0 MiB           1       return x


Время выполнения функции wrapper заняло 0.5759997367858887 секунд
Время выполнения timeit составило  0.0003367000000000786  секунд
"""

@decor
@profile
def task_1_2():
    z=list(range(10000))
    return z

print('Время выполнения timeit составило ',
    timeit.timeit(
        "task_1_2",
        globals=globals(),
        number=10000) ,' секунд')
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    40     19.8 MiB     19.8 MiB           1   @decor
    41                                         @profile
    42                                         def task_1_2():
    43     20.1 MiB      0.3 MiB           1       z=list(range(10000))
    44     20.1 MiB      0.0 MiB           1       return z


Время выполнения функции wrapper заняло 0.0030090808868408203 секунд
Время выполнения timeit составило  0.0003379000000000021  секунд
"""

"""
По 1 заданию можно сделать вывод , что обе функции занимают 
одинаково количество оперативной памяти, но 2 выполняется
быстрее из за того , что это встроенная функция
"""
#2
@decor
@profile
def task_2_1():
    a=[]
    for i in range(100000):
        a.append(i)
    return a

print('Время выполнения timeit составило ',
    timeit.timeit(
        "task_2_1",
        globals=globals(),
        number=100000) ,' секунд')
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    72     19.5 MiB     19.5 MiB           1   @decor
    73                                         @profile
    74                                         def task_2_1():
    75     19.5 MiB      0.0 MiB           1       a=[]
    76     23.6 MiB      0.1 MiB      100001       for i in range(100000):
    77     23.6 MiB      4.0 MiB      100000           a.append(i)
    78     23.6 MiB      0.0 MiB           1       return a


Время выполнения функции wrapper заняло 10.629982233047485 секунд
Время выполнения timeit составило  0.0035032000000008168  секунд
"""

@decor
@profile
def task_2_2():
    a=[]
    for i in range(100000):
        a.insert(0 ,i)
    return a

print('Время выполнения timeit составило ',
    timeit.timeit(
        "task_2_2",
        globals=globals(),
        number=100000) ,' секунд')


"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    94     23.6 MiB     23.6 MiB           1   @decor
    95                                         @profile
    96                                         def task_2_2():
    97     23.6 MiB      0.0 MiB           1       a=[]
    98     27.8 MiB      0.1 MiB      100001       for i in range(100000):
    99     27.8 MiB      4.2 MiB      100000           a.insert(0 ,i)
   100     27.8 MiB      0.0 MiB           1       return a


Время выполнения функции wrapper заняло 16.58099913597107 секунд
Время выполнения timeit составило  0.003234700000000146  секунд
"""

"""
Видно , что во втором случае оперативной памяти занимается больше
+append работает быстрее insert
"""
#3
@decor
@profile
def task_3_1():
    sum=[]
    for i in range(100000):
        if i % 5 == 0:
            sum.append(i)
    return sum

print('Время выполнения timeit составило ',
    timeit.timeit(
        "task_3_1",
        globals=globals(),
        number=100000) ,' секунд')

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   118     19.1 MiB     19.1 MiB           1   @decor
   119                                         @profile
   120                                         def task_3_1():
   121     19.1 MiB      0.0 MiB           1       sum=[]
   122     19.8 MiB      0.0 MiB      100001       for i in range(100000):
   123     19.8 MiB      0.6 MiB      100000           if i % 5 == 0:
   124     19.8 MiB      0.2 MiB       20000               sum.append(i)
   125     19.8 MiB      0.0 MiB           1       return sum


Время выполнения функции wrapper заняло 10.49242377281189 секунд
Время выполнения timeit составило  0.0033621000000003676  секунд
"""

@decor
@profile
def task_3_2():
    sum = [x for x in range(100000) if x%5 == 0]
    return sum

print('Время выполнения timeit составило ',
    timeit.timeit(
        "task_3_2",
        globals=globals(),
        number=100000) ,' секунд')

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   130     19.8 MiB     19.8 MiB           1   @decor
   131                                         @profile
   132                                         def task_3_2():
   133     20.8 MiB      1.0 MiB      100003       sum = [x for x in range(100000) if x%5 == 0]
   134     20.8 MiB      0.0 MiB           1       return sum


Время выполнения функции wrapper заняло 4.770271062850952 секунд
Время выполнения timeit составило  0.00400109999999998  секунд
"""

"""
Вторая функция работает гораздо быстрее , чем
первая , потому что всегда цикл в 1 строку будет работать быстрее ,
но оперативной памяти , как мы видим , второй вариант занимает больше
"""





