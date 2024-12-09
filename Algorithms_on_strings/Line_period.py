"""
Дана непустая строка s. Нужно найти такое наибольшее число k и строку t,
что s совпадает со строкой t, выписанной k раз подряд.

Ограничение времени - 1 секунда.

Входные данные
Одна строка длины N, 0 < N ≤ 10^6,
состоящая только из маленьких латинских букв.

Выходные данные
Одно число - наибольшее возможное k.
"""


def pref_func(s):
    n = len(s)
    prefix = [0] * n
    for i in range(1, n):
        curr = prefix[i - 1]
        while curr > 0 and s[i] != s[curr]:
            curr = prefix[curr - 1]
        if s[i] == s[curr]:
            curr += 1
        prefix[i] = curr
    return prefix


def find_max_k(s):
    n = len(s)
    prefix = pref_func(s)
    len_t = n - prefix[-1]
    if n % len_t == 0:
        return n // len_t
    else:
        return 1


s = str(input())
print(find_max_k(s))
