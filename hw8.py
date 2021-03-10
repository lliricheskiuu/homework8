# 1. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Буквы в строке МОГУТ повторяться (перемешивание алфавита не подойдет, так как буквы не смогут повторяться)

import random as rnd
import string

MIN, MAX = 100, 999

names = ['Kirill', 'Anna', 'Jacob']
domains = ['com', 'ua', 'net']
length = rnd.randint(5, 7)


def generate_rnd_str() -> str:
    letters = string.ascii_lowercase
    random_str = ''.join(rnd.choice(letters) for i in range(length))
    return random_str


def generate_rnd_mail(rnd_name, rnd_domain):
    mail = f'1) {rnd_name[rnd.randint(0, len(rnd_name) - 1)]}.{rnd.randint(MIN, MAX)}@' \
           f'{generate_rnd_str()}.{rnd_domain[rnd.randint(0, len(rnd_domain) - 1)]}'
    return mail


e_mail = generate_rnd_mail(names, domains)
print(e_mail)

###

# 2. Написать функцию, которая генерирует и возвращает строку случайной длинны.
# Минимальную и максимальную длину строки ограничить с помощью параметров min_limit, max_limit, передаваемых в функцию.


def generate_rnd_str_with_limits(min_l: int, max_l: int) -> str:
    letters = string.ascii_lowercase
    rnd_int = rnd.randint(min_l, max_l)
    random_str = ''.join(rnd.choice(letters) for i in range(rnd_int))
    return random_str


min_lim = int(input("\nEnter min lim:"))
max_lim = int(input("Enter max lim:"))

print(f"\n2) Your string:\n{generate_rnd_str_with_limits(min_lim, max_lim)}")

###

# 3. Написать функцию (или последовательность нескольких функций), которые преобразуют случайную строку,
# полученную в п 2 по следующим правилам:
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы,
# знаки препинания, символ перехода на новую строку (\n).
# Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
# Под словом будем понимать набор случайных букв от одной до 10.
# Большие буквы только в начале слов. Цифры не должны быть частями слов, а стоять отдельно.
# Знаки препинания всегда идут в конце слова.


def create_spaces(rnd_string: str) -> str:
    index = 0
    rnd_listed_str = list(rnd_string)
    tmp = True
    while tmp:
        step = rnd.randint(1, 10)
        index += step
        if index < len(rnd_string):
            rnd_listed_str[index] = ' '
        else:
            tmp = False
    rnd_string = ''.join(rnd_listed_str)
    return rnd_string


def modify_word(word: str, chance=4) -> str:
    if rnd.randint(1, 10) < chance:
        word = word.capitalize()
    if rnd.randint(1, 14) < chance:
        word += ','
    if rnd.randint(1, 14) < chance:
        word += '\n'
    return word


def modify_word_into_digits(word: str, chance=4) -> str:
    if rnd.randint(1, 20) < chance:
        list_word = list(word)
        list_word.clear()
        for symbol in range(len(word)):
            list_word.append(str(rnd.randint(1, 10)))
        word = ''.join(list_word)
    return word


def modify_str(rnd_string: str) -> str:
    rnd_split_str = rnd_string.split()
    result = []
    rnd_split_str[0] = rnd_split_str[0].capitalize()
    rnd_split_str[-1] += '.'
    result.append(rnd_split_str[0])
    for word in rnd_split_str[1:-1]:
        word = modify_word(word)
        word = modify_word_into_digits(word)
        result.append(word)
    result.append(rnd_split_str[-1])
    return " ".join(result)


rnd_str = generate_rnd_str_with_limits(0, 100)
rnd_str = create_spaces(rnd_str)
rnd_str = modify_str(rnd_str)

print(f"\n3) Result:\n {rnd_str}")
