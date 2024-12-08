"""
Найти все вхождения строки T в строку S.

Входные данные
Первые две строки входных данных содержат строки S  и T, соответственно.
Длины строк больше 0 и меньше 50000, строки содержат только строчные латинские буквы.

Выходные данные
Выведите номера символов, начиная с которых строка T входит в строку S, в порядке возрастания.
"""


def z_func(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        k = max(0, min(z[i - l], r - i))
        while i + k < n and s[k] == s[i + k]:
            k += 1
        z[i] = k
        if i + k > r:
            l, r = i, i + k
    return z


def find(S, T):
    combined = T + "#" + S
    z = z_func(combined)
    result = []
    t_len = len(T)
    for i in range(t_len + 1, len(combined)):
        if z[i] == t_len:
            result.append(i - t_len - 1)

    return result


S = str(input())
T = str(input())

answer = find(S, T)
print(*answer)
