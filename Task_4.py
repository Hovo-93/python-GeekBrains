"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове."""

line = input('Введите слова, разделенные пробелами ').split()
for i, value in enumerate(line):
    print(i, value[:10])
