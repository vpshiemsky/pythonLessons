"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""
def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    else:
        return a / b


def is_correct_operator(operator):
    return operator == '0' or operator == '+' or operator == '-' or operator == '*' or operator == '/'


def get_operator():
    return input('Введите оператор (+,-,*,/) 0 - выход: ')


def run_calculator(a=None, b=None):
    if a is None:
        a = float(input('Введите перове число : '))
    if b is None:
        b = float(input('Введите второе число : '))
    operator = get_operator()

    if not is_correct_operator(operator):
        print('Это не оператор')
        run_calculator(a, b)
        return
    elif operator == '0':
        return
    elif operator == '/' and b == 0:
        print('На ноль делить нельзя ')
        run_calculator()
        return
    else:
        print(calculate(a, b, operator))
        run_calculator()


run_calculator()