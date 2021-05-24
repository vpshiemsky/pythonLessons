""""
Задание 6.
Задание на закрепление навыков работы с очередью
Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""
class Task_class:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


if __name__ == '__main__':
    qc_obj = Task_class()

def tasks(zadacha, num):

    queue_obj = Task_class()
    for task_ in zadacha:
        queue_obj.to_queue(task_)
    a = True
    summ = []
    while a:
        print('G - выход , A - продолжить')
        user = input(': ')
        if user == 'A' or user == 'a' or user == 'а' or user == 'А':
            a = int(input('Введите перове число  '))
            b = int(input('Введите второе число  '))

            print(f'Сумма - {a + b}')
            c.append(a + b)
            print(f'Общая сумма - {summ}')
        elif user == 'g' or user == 'G':
            a = False

    while queue_obj.size() > 1:
        for i in range(num):
            queue_obj.to_queue(queue_obj.from_queue())
        queue_obj.from_queue()
    return queue_obj.from_queue()








