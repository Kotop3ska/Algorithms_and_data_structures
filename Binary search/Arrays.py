"""
Дано два массива. Для каждого элемента второго массива определите, сколько раз он встречается в первом массиве.

Входные данные
Первая строка входных данных содержит одно число N (1 ≤ N ≤ 105) – количество элементов в первом массиве. 
Далее идет N целых чисел, не превосходящих по модулю 109 – элементы первого массива, 
Далее идет количество элементов M во втором массиве и M элементов второго массива с такими же ограничениями.

Выходные данные
Выведите M чисел: для каждого элемента второго массива выведите, сколько раз такое значение встречается в первом массиве.
"""

def binary_search_left(arr, x):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] < x:
            l = m
        else:
            r = m
    return r


def binary_search_right(arr, x):
    l = -1
    r = len(arr)
    while r - l > 1:
        m = (l + r) // 2
        if arr[m] <= x:
            l = m
        else:
            r = m
    return l


def count(first_array, second_array):
    first_array.sort()
    result = []
    for x in second_array:
        left = binary_search_left(first_array, x)
        right = binary_search_right(first_array, x)
        if left == len(first_array) or first_array[left] != x:
            result.append(0)
        else:
            result.append(right - left + 1)
    return result


n = int(input())
arr1 = [int(x) for x in input().split()]
m = int(input())
arr2 = [int(x) for x in input().split()]

result = count(arr1, arr2)
print(*result)