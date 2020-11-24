"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно."""

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):
    def calc(self, V):
        coat_res = round(V / (6.5 + 0.5))
        return f'Расхода ткани для палто {coat_res}'


class Costume(Clothes):
    def calc(self, H):
        cost_res = 2 * H + 0.3
        return f'Расхода ткани для костюма {cost_res}'


class Total(Clothes):
    def calc(self, V, H):
        total_res = (round(V / 6.5 + 0.5)) + (2 * H + 0.3)
        return f'Общий расход ткани {total_res}'


a = Coat()
print(a.calc(42))
b = Costume()
print(b.calc(25))
c = Total()
print(c.calc(42, 175))
