"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости."""

import random


class Car:
    def __init__(self, speed, color, name, is_police=bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась!")

    def turn(self):
        direction = ["to the left", "to the right"]
        l = random.choice(direction)
        print(f"Машина повернула {l}")

    def show_speed(self):
        print(f"Скорость автомобиля: {self.speed} км/ч")

    def show_type(self):
        print("Машина")


class TownCar(Car):
    def show_type(self):
        print("Городская машина")

    def show_speed(self):
        print(f"Скорость автомобиля: {self.speed} км/ч")
        if self.speed > 60:
            print("Превышение скорости")


class SportCar(Car):
    def show_type(self):
        print("Спортивная машина")


class WorkCar(Car):
    def show_type(self):
        print("Служебная машина")

    def show_speed(self):
        print(f"Скорость автомобиля: {self.speed} км/ч")
        if self.speed > 40:
            print("Превышение скорости")


class PoliceCar(Car):
    def show_type(self):
        print("Полицеская машина")


a = Car(120, "red", "Mazda", is_police=True)
a.go()
a.show_speed()
a.show_type()
a.turn()
a.stop()
print(a.speed)
