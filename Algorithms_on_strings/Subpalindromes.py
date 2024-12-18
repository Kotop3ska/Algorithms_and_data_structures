"""
Строка называется палиндромом, если она читается одинаково как слева направо, так и справа налево.
Например, строки abba, ata являются палиндромами.

Дана строчка. Ее подстрокой называется некоторая непустая последовательность подряд идущих символов.
Напишите программу, которая определит, сколько подстрок данной строки является палиндромами.

Входные данные
Вводится одна строка, состоящая из маленьких латинских букв. Длина строки не превышает 100000 символов.

Выходные данные
Выведите одно число — количество подстрок данной строки, являющихся палиндромами
"""


def manacher(text):
    n = len(text)
    count = 0
    c = 0
    r = 0
    p = [0] * n
    for i in range(n):
        mirror = 2 * c - i
        if i < r:
            p[i] = min(r - i, p[mirror])

        while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and text[i + p[i] + 1] == text[i - p[i] - 1]:
            p[i] += 1

        if i + p[i] > r:
            c = i
            r = i + p[i]

        count += (p[i] + 1) // 2

    return count


text = input()
text_split = '#' + '#'.join(text) + '#'
print(manacher(text_split))
