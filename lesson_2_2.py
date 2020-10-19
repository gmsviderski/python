"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
my_list = list(map(int, input('Введите через пробел целые числа: ').split()))
if len(my_list) % 2 == 0:
    for i in range(0, len(my_list) - 1, 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
else:
    for i in range(0, len(my_list) - 2, 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)
