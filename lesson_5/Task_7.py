"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки."""
import json

with open("7file.txt", "r", encoding='utf-8') as f:
    line = f.readlines()

    general_list = []
    title_list = []
    profit = []
    count = 0
    total = 0
    for i in line:
        title, form, proceeds, cost = i.split()
        title_list.append(title)
        summa = int(proceeds) - int(cost)
        profit.append(summa)
    if summa > 0:
        total += summa
        count += 1
    average_profit = total / count
    dict_1 = dict(zip(title_list, profit))
    dict_2 = dict(Средняя_прибыль=average_profit)
    print(dict_1)
    print(dict_2)
    general_list.append(dict_1)
    general_list.append(dict_2)

with open("my_file.json", "w") as write_f:
    json.dump(general_list, write_f)
