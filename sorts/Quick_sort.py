"""Отсортируйте данный массив. Используйте быструю сортировку.

Входные данные
Первая строка входных данных содержит количество элементов в массиве N, N ≤ 105. 
Далее идет N целых чисел, не превосходящих по абсолютной величине 10^9. 

Выходные данные
Выведите эти числа в порядке неубывания."""

from random import randint


def quick_sort(A, left, right):
    if left < right:
        val = A[randint(left, right)]
        l, r = left, right
        while l <= r:
            while A[l] < val:
                l += 1
            while A[r] > val:
                r -= 1
            if l <= r:
                A[l], A[r] = A[r], A[l]
                l += 1
                r -= 1
        if left < r:
            quick_sort(A, left, r)
        if right > l:
            quick_sort(A, l, right)


N = int(input())
A = [int(x) for x in input().split()]

quick_sort(A, 0, len(A) - 1)

print(' '.join(str(x) for x in A))
