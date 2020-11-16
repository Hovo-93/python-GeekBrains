"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран."""

with open("6file.txt", "r", encoding='utf-8') as f:
    subject = []
    sum_list = []
    while True:
        line = f.readline().split()
        if not line:
            break
        summa = 0
        for i in line:
            if chr(48) <= i < chr(58):
                summa += int((i.split("(")[0]))
                name = line[0]
                subject.append(name)
                sum_list.append(summa)
    print(dict(zip(subject, sum_list)))

