# Пользователь вводит месяц в виде целого числа от 1 до 12.

seasons_list = ['Winter', 'Spring', 'Summer', 'Autumn']
seasons_dict = {1: "Зима",
         2: "Весна",
         3: "Лето",
         4: "Осень"}
month = int(input(f"введите число месяца: "))
if month ==1 or month == 2 or month == 12:
    print(seasons_list[0], seasons_dict.get(1))
elif month ==3 or month == 4 or month == 5:
    print(seasons_list[1], seasons_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2], seasons_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3], seasons_dict.get(4))
else:
    print('Такого месяца нет!')

# Написала вывод обоих решений в одну строку(print) чтобы код бы не такой длинный.