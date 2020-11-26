"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата."""


class ComplexNum:
    def __init__(self, digits):
        self.digits = digits

    def __str__(self):
        return f'{self.digits}'

    def __add__(self, other):
        return ComplexNum(self.digits + other.digits)

    def __mul__(self, other):
        return ComplexNum(self.digits * other.digits)


a = ComplexNum(-5 - 1j)
b = ComplexNum(-1 + 1j)
print(a + b)
print(a * b)
