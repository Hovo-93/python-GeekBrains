"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class Error(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = input("Введите делимое: ")
divider = input("Введите делитель: ")

try:
    result = int(dividend) / int(divider)
    if divider == 0:
        raise Error("На ноль делить нельзя")
except ValueError:
    print("Вы ввели не число")
except (Error, ZeroDivisionError) as e:
    print(e)
else:
    print(f"Ответ: {result}")
finally:
    print('Конец')
