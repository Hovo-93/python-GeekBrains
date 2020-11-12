"""2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента."""
from random import randrange

my_list = []
while len(my_list) != 10:
    my_list.append(randrange(1, 99))
new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1]]
print(new_list)
