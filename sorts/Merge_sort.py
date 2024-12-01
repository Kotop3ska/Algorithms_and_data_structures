"""
Отсортируйте данный массив, используя сортировку слиянием.
Входные данные
Первая строка входных данных содержит количество элементов в массиве N, N ≤ 105. 
Далее идет N целых чисел, не превосходящих по абсолютной величине 109.
Выходные данные
Выведите эти числа в порядке неубывания.
"""

N = int(input())
A = [int(x) for x in input().split()]


def merge_sort(A):
    if len(A) <= 1:
        return A
    ind = len(A) // 2
    left = merge_sort(A[:ind])
    right = merge_sort(A[ind:])
    return merge(left, right)


def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    if i < len(left):
        res.extend(left[i:])
    if j < len(right):
        res.extend(right[j:])
    return res


res = ' '.join(str(i) for i in merge_sort(A))
print(res)