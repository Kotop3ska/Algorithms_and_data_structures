"""
Реализуйте алгоритм приближенного бинарного поиска.

Входные данные
В первой строке входных данных содержатся числа 𝑁 и 𝐾 (0<𝑁,𝐾<100001).
Во второй строке задаются 𝑁 чисел первого массива, отсортированного по неубыванию, 
а в третьей строке – 𝐾 чисел второго массива. Каждое число в обоих массивах по модулю не превосходит 2⋅10^9.

Выходные данные
Для каждого из 𝐾 чисел выведите в отдельную строку число из первого массива, наиболее близкое к данному. 
Если таких несколько, выведите меньшее из них.
"""

N, K = map(int, input().split())

arr_1 = [int(x) for x in input().split()]
arr_2 = [int(x) for x in input().split()]


def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    if abs(arr[l] - x) < abs(arr[r] - x):
        num = arr[l]
    else:
        num = arr[r]
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x:
            num = x
            return num
        elif arr[m] < x:
            l = m + 1
        else:
            r = m - 1

        if abs(arr[m] - x) < abs(num - x):
            num = arr[m]
        if abs(arr[m] - x) == abs(num - x):
            if num > arr[m]:
                num = arr[m]

    return num


for x in arr_2:
    print(binary_search(arr_1, x))