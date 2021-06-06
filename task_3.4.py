"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import timeit
import cProfile
# быстрее всего отработала на срезах
# По профилированию могу сказать только то , что
# было больше всего вызовов => самое большое время
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

number = int(input('Введите целое число : '))

revers_1(number, revers_num=0)
revers_2(number, revers_num=0)
revers_3(number)


print(
    'Рекурсия наоборот : ',
    timeit(
        f'revers_1({number})',
        globals=globals(),
        number=10000))
print(
    'Наоборот в цикле : ',
    timeit(
        f'revers_2({number})',
        globals=globals(),
        number=10000))
print(
    'Наоборот на срезах : ',
    timeit(
        f'revers_3({number})',
        globals=globals(),
        number=10000))

cProfile.run('revers_1(10000000000)')
cProfile.run('revers_2(10000000000)')
cProfile.run('revers_3(10000000000)')