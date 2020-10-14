"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
number_str_in = input('Введите целое число N = ')
number_int = int(number_str_in)
ans = 0
while number_int > 0:
    ans += int(number_str_in * number_int)
    number_int -= 1
print(f'Сумма чисел N+NN+NNN.... равна = {ans}')
