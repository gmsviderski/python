"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(var1, var2, var3):
    my_list = list()
    my_list.append(var1)
    my_list.append(var2)
    my_list.append(var3)
    my_list.sort()
    return my_list[-1] + my_list[-2]


a, b, c = map(int, input('Введите 3 целых числа через пробел: ').split())
print(my_func(a, b, c))
