"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

with open("3file.txt", "r", encoding='utf-8') as file:
    line = file.readlines()
    income = 0
    total = 0
    count = 0
    k = {}
    for i in line:
        key, value = i.split()
        total += int(value)
        count += 1
        k[key] = value
        if int(value) < 20000:
            print(f'{key}: зарплата меньше 20000')
    income = total / count

    print(f"Средний доход - {income}")
