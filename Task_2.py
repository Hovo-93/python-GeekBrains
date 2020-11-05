"""2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
 При нечетном количестве элементов последний сохранить на своем месте.
  Для заполнения списка элементов необходимо использовать функцию input()"""

count_of_el = int(input("Введите количество элементов списка "))
some_list = []
while count_of_el != len(some_list):
    el = input(f"Введите {len(some_list) + 1} элемент списка: ")
    some_list.append(el)
for i in range(1, len(some_list), 2):
    some_list[i - 1], some_list[i] = some_list[i], some_list[i - 1]
print(some_list)
