"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов."""


def my_func(*args):
    """
    1-ое решение ))
    """
    args = input('Ввод чисел с пробелами ').split()
    if len(args) > 3:
        print('Error')
        exit()
    max = int(args[0])
    mas = []
    for i in range(len(args)):
        if int(args[i]) > max:
            max = int(args[i])
            mas.append(int(max))
    return (sum(mas))


# 2 простое решение
def my_func(var_1, var_2, var_3):
    return (var_1 + var_2 + var_3) - min(var_1, var_2, var_3)
