# Для списка реализовать обмен значений соседних элементов.

list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
ch = 0
for i in range(int(len(list) / 2)):
    list[ch], list[ch + 1] = list[ch + 1], list[ch]
    ch += 2
print(list)