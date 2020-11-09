"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def division(arg1, arg2):
    try:

        result = arg1 / arg2
    except ZeroDivisionError:
        return "You cannot divide by zero!"
    return round(result)
