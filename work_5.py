# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.

my_list = [7, 5, 3, 3, 2]
for i in range(1):
    new_num = int(input(f"Введите целое число: "))
    my_list.append(new_num)
my_list.sort()
my_list.reverse()
print(my_list)