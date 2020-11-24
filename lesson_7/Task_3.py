"""3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов"""


class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        a = self.quantity
        b = other.quantity
        c = a + b
        return c

    def __sub__(self, other):
        c_1 = self.quantity
        c_2 = other.quantity
        c_3 = c_1 - c_2
        return c_3

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        if self.quantity == 0:
            return "Делить на 0 нельзя"
        else:
            return self.quantity // other.quantity

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cells1 = Cell(33)
cells2 = Cell(9)
print(cells1 + cells2)
print(cells1 - cells2)
print(cells1.make_order(10))
print(cells1 / cells2)
