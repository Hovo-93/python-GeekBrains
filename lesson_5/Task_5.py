"""5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

str_list = input("Введите текст разделяя пробелами ").split()

with open("5file.txt", "w") as file:
    for line in str_list:
        file.write(line + '\n')


with open("5file.txt", "r") as file:
    total = 0
    arr = [int(line) for line in str_list]
    total = sum(arr)
    print(total)
