"""
Найти все вхождения строки T в строку S.

Входные данные
Первые две строки входных данных содержат строки S  и T, соответственно.
Длины строк больше 0 и меньше 50000, строки содержат только строчные латинские буквы.

Выходные данные
Выведите номера символов, начиная с которых строка T входит в строку S, в порядке возрастания.
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


def find(S, T):
    combined = T + "#" + S
    pref = pref_func(combined)
    result = []
    t_len = len(T)
    for i in range(t_len + 1, len(combined)):
        if pref[i] == t_len:
            result.append(i - 2 * t_len)

    return result


S = str(input())
T = str(input())

answer = find(S, T)
print(*answer)
