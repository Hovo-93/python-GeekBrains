"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def division(*args):
    try:
        arg1 = int(input('Input dividend '))
        arg2 = int(input('Input divider '))
        result = arg1 / arg2
    except ZeroDivisionError:
        return "You cannot divide by zero!"
    return round(result)
