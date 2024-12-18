"""
Дана строка S, состоящая из N символов.
Определим функцию A(i) от первых i символов этой сроки следующим образом:

A(i) = максимально возможному k, что равны следующие строки:

S[1]+S[2]+S[3]+…+S[k]

S[i]+S[i–1]+S[i–2]+…+S[i–k+1]

где S[i] – i-ый символ строки S, а знак + означает,
что символы записываются в строчку непосредственно друг за другом.

Напишите программу, которая вычислит значения функции
A для заданной строчки для всех возможных значений i от 1 до N.

Входные данные
В первой строке входного файла записано одно число N. 1≤N≤200000.
Во второй строке записана строка длиной N символов, состоящая только из больших и/или маленьких латинских букв.

Выходные данные
В выходной файл выведите N чисел — значения функции A(1), A(2), … A(N).
"""


def a_func(s):
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


n = int(input())
s = input()

s += s[::-1]
print(*a_func(s)[-1: n - 1: -1])
