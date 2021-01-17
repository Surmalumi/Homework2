# Создать список и заполнить его элементами различных типов данных.

list = [None, -10, 'Star', True, 9.5]
def my_type(el):
    for el in range(len(list)):
        print(type(list[el]))
    return
my_type(list)

