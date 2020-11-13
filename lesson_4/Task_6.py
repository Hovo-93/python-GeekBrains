"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения."""

from itertools import count, cycle

# 1
for el in count(3):
    if el == 11:
        break
    else:
        print(el)

# 2
mass = ['A', 'B', 'C']
counter = 0
for el in cycle(mass):
    if counter > 5:
        break
    print(el)
    counter += 1
