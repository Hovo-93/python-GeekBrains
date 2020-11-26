"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка."""


class Error(Exception):
    def __init__(self, txt):
        self.txt = txt


new_arr = []
while True:
    try:
        input_str = input('Введите число: ')
        new_digits = input_str
        if input_str == 'stop':
            exit()
        if new_digits.isalpha():
            raise Error("Вы ввели не число")
        if new_digits.isdigit():
            new_arr.append(new_digits)
    except Error as e:
        print(e)
    finally:
        print(new_arr)
