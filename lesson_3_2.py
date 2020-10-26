"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def information(name, fam, birth, city, email, tel):
    def_dict = dict()
    def_dict['name'] = name
    def_dict['fam'] = fam
    def_dict['birth'] = birth
    def_dict['city'] = city
    def_dict['email'] = email
    def_dict['tel'] = tel
    return def_dict


my_dict = information(name='Genry',
                      fam='Sviderski',
                      birth='1968',
                      city='Cherepovets',
                      email='nomail@mail.ru',
                      tel='123456')
for i in my_dict.values():
    print(i, end=' ')
