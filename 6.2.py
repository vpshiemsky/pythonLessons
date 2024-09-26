"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Подсказка:
Базовый случай здесь - угадали число или закончились попытки
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

import random
def guess(count, number):
    print(f'Попытка №{count} ')
    answer = int(input('Введите число от 0 до 100 : '))
    if count == 10 or answer == number:
        if answer == number:
            print('Верно ')
        print(f'Загаданное число : {number}')
    else :
        if answer > number :
            print(f'Много ')
        else :
            print(f'Мало ')
        guess(count + 1, number)

guess(1,random.randint(0, 100))