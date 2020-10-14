"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
number_in = int(input('Введите целое положительное число: '))
max_digit = number_in % 10
while number_in > 0:
    number_in //= 10
    if max_digit < number_in % 10:
        max_digit = number_in % 10
print(f'Самая большая цифра в введенном числе = {max_digit}')
