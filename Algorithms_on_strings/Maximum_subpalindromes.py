"""
Дана непустая строка, длина которой не превышает 10^6.
Требуется для каждой позиции  символа в строке найти длину наибольшего палиндрома с центром в этом символе.
Строка состоит из букв английского алфавита, большие и маленькие буквы считаются различными.
Ограничение времени - 1 секунда.

Входные данные
Одна строка длины N, 0 < N ≤ 10^6.

Выходные данные
N чисел, разделенные пробелами.
"""


def manacher(text):
    n = len(text)
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

    return p


text = str(input())
result = manacher(text)
palindrome_lengths = [2 * radius + 1 for radius in result]
print(*palindrome_lengths)
