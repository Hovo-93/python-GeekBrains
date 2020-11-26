"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен
проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
import datetime as dt


class Date:

    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    def __str__(self):
        date = dt.datetime.strptime(self.day_month_year, '%d-%m-%Y').date()
        return f'Преобразование строки в дату {date}'

    @classmethod
    def number(cls, day_month_year):
        my_date = []
        for el in day_month_year.split():
            if el != '-':
                my_date.append(el)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if (day > 31 or day < 1) or (month < 1 or month > 12) or (year < 1000 or year > 3000):
            return f"Введена некорректная дата"


today = Date('25-11-2020')
print(today)
print(Date.number('11 - 11 - 2011'))
print(today.valid(15, 22, 3000))
print(Date.valid(10,12,2020))
