"""4. Создать (не программно) текстовый файл со следующим содержимым:"""

with open("4file.txt", "r", encoding='utf-8') as file:
    line = file.readlines()
    key = []
    value = []
    for i in line:
        key.append(i.split()[0])
        value.append(i.split()[2])

    new_key = []
    for j in key:
        if 'One' in j:
            new_key.append(j.replace('One', 'Один'))
        if 'Two' in j:
            new_key.append(j.replace('Two', 'Два'))
        if 'Three' in j:
            new_key.append(j.replace('Three', 'Три'))
        if 'Four' in j:
            new_key.append(j.replace('Four', 'Четыре'))

with open("4filenew.txt", "w", encoding='utf-8') as new_file:
    new_file.write(f"{new_key[0]} - {value[0]}\n")
    new_file.write(f"{new_key[1]} - {value[1]}\n")
    new_file.write(f"{new_key[2]} - {value[2]}\n")
    new_file.write(f"{new_key[3]} - {value[3]}")
