"""7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить
только первые n чисел, начиная с 1! и до n!."""


def fact(n):
    factorial = 1
    for i in range(2, n + 1):
        yield i
        factorial *= i
    yield factorial


for el in fact(4):
    print(el)
