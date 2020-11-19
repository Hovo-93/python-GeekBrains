"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода."""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._mas = 25
        self._thickness = 5

    def calc_the_mass(self):
        mass = round((self._length * self._width * self._mas * self._thickness) / 1000)
        return mass

    def print(self):
        return f"Масса асфальта составляет: {self.calc_the_mass()} т"


a = Road(20, 5000)
print(a.print())
