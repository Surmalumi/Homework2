# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.

goods =[]
features = {}
goods_dict = {'name': None,
               'price': None,
               'qty': None,
               'type': None}
while True:
    continue_check = input('Continue: ')
    if continue_check == 'No':
        break
    goods_dict['name'] = input("Введите название товара: ")
    goods_dict['price'] = input("Введите цену: ")
    goods_dict['qty'] = input("Введите количество: ")
    goods_dict['type'] = input("Введите тип товара: ")
    goods.append(goods_dict.copy())
print(f' Информация о товаре: {goods}')

# Не доделала задачу как это было запрошено в задании.(