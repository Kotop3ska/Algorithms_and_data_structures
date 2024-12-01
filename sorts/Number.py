"""
Вася написал на длинной полоске бумаги большое число и решил похвастаться своему старшему брату Пете этим достижением. 
Но только он вышел из комнаты, чтобы позвать брата, 
как его сестра Катя вбежала в комнату и разрезала полоску бумаги на несколько частей. 
В результате на каждой части оказалось одна или несколько идущих подряд цифр.
Теперь Вася не может вспомнить, какое именно число он написал. Только помнит, что оно было очень большое. 
Чтобы утешить младшего брата, Петя решил выяснить, 
какое максимальное число могло быть написано на полоске бумаги перед разрезанием. Помогите ему!

Входные данные
Входные данные состоят из одной или более строк, каждая из которых содержит последовательность цифр. 
Количество строк  не превышает 100, каждая строка содержит от 1 до 100 цифр. 
Гарантируется, что хотя бы в одной строке первая цифра отлична от нуля.

Выходные данные
Выведите одну строку – максимальное число, которое могло быть написано на полоске перед разрезанием.
"""

from sys import stdin
from functools import cmp_to_key


def cmp(x, y):
    if x + y < y + x:
        return 1
    return -1


lines = [line.rstrip() for line in stdin]
ls = sorted(lines, key=cmp_to_key(cmp))
print(''.join(ls))
