"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""
Printer_count = 10
Scanner_count = 20
Xerox_count = 30


class Sklad_Orgtexnika():

    def plus(p, x, sc):
        total = {"принтеров": p, "ксероксов": x, "сканнеров": sc}
        Printer.count = Printer_count + p
        Xerox.count = Xerox_count + x
        Scanner.count = Scanner_count + sc
        return f"Принято на склад: {total}"

    @staticmethod
    def total():
        return f"Всего на складе: {Printer.count} принтеров, {Scanner.count} сканнеров и {Xerox.count} ксероксов"

    def transfer(p, x, sc):
        total = {"принтеров": p, "ксероксов": x, "сканнеров": sc}
        Printer.count = Printer_count - p
        Xerox.count = Xerox_count - x
        Scanner.count = Scanner_count - sc
        return f"В подразделение №105 передано {total}"


class OrgTexnika:
    def __init__(self, count):
        self.count = count


class Printer(OrgTexnika):
    count = Printer_count
    print_speed = 50


class Scanner(OrgTexnika):
    count = Scanner_count
    scan_speed = 40


class Xerox(OrgTexnika):
    count = Xerox_count
    xerox_speed = 20


o = Sklad_Orgtexnika

try:
    p = int(input("Cколько принтеров хотите добавить на склад "))
    sc = int(input("Cколько сканнеров хотите добавить на склад "))
    x = int(input("Cколько ксероксов хотите добавить на склад "))
except ValueError:
    print("Введите число")
else:
    print(o.plus(p, x, sc))
    print(o.total())
