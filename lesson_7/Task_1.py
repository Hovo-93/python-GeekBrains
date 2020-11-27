"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы."""

import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.matrix)

    def __add__(self, other):
            A = np.array(self.matrix)
            B = np.array(other.matrix)
            C = A + B
            return Matrix(C)


a = Matrix([[1, 2], [3, 4], [5, 6]])
b = Matrix([[7, 8], [9, 1], [2, 6]])
print(a + b)
