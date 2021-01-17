# Пользователь вводит строку из нескольких слов, разделённых пробелами.

words = input(f"Введите строку из нескольких слов с пробелами: ")
my_word = words.split()
for i, el in enumerate(my_word, 1):
    if len(el) > 10:
        el = el[1:10]
    print(f'{i}. {el}')