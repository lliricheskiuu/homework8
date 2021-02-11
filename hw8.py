# 1. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Буквы в строке МОГУТ повторяться (перемешивание алфавита не подойдет, так как буквы не смогут повторяться)

import random as rnd
import string

names = ['Zarechnuy', 'Sokolow', 'Ymanez']
domains = ['com', 'ua', 'net']
length = rnd.randint(5, 7)


def generate_rnd_str():
    letters = string.ascii_lowercase
    rand_str = ''.join(rnd.choice(letters) for i in range(length))
    return rand_str


def generate_rnd_mail():
    mail = f'{names[rnd.randint(0, 2)]}.{rnd.randint(100, 999)}@{generate_rnd_str()}.{domains[rnd.randint(0, 2)]}'
    return mail


e_mail = generate_rnd_mail()
print(e_mail)

###

# 2. Написать функцию, которая генерирует и возвращает строку случайной длинны.
# Минимальную и максимальную длину строки ограничить с помощью параметров min_limit, max_limit, передаваемых в функцию.


def generate_random_str(min_l, max_l):
    letters = string.ascii_lowercase
    rand_str = ''.join(rnd.choice(letters) for i in range(min_l, max_l))
    return rand_str


min_lim = int(input("Enter min lim:"))
max_lim = int(input("Enter max lim:"))

print(generate_random_str(min_lim, max_lim))

###

# 3. Написать функцию (или последовательность нескольких функций), которые преобразуют случайную строку,
# полученную в п 2 по следующим правилам:
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы,
# знаки препинания, символ перехода на новую строку (\n).
# Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
# Под словом будем понимать набор случайных букв от одной до 10.
# Большие буквы только в начале слов. Цифры не должны быть частями слов, а стоять отдельно.
# Знаки препинания всегда идут в конце слова.

