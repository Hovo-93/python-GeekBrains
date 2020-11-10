month = int(input("Введите месяц в виде целого числа от 1 до 12 "))
if month > 12 or month < 1:
    print('Error')

seasons = {
    'Зима': [12, 1, 2],
    'Весна': [3, 4, 5],
    'Лето': [6, 7, 8],
    'Осень': [9, 10, 11],
}

for key, value in seasons.items():
    if month in value:
        print(f"{month} месяц относится к {key}")
