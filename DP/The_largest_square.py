"""
Дан двумерный массив целых чисел n×m, все элементы которого — нули или единицы.
Найти в нём наибольший по площади квадрат, состоящий только из единиц.
Гарантируется, что в нём есть хотя бы одна единица.

Входные данные
Вводятся два целых числа n и m (1≤n,m≤1000), а потом n строк по m чисел 0 или 1 — элементы массива.

Выходные данные
Вывести три числа — длину стороны квадрата и координаты его левого верхнего угла.
"""


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

max_side = 0
top_left = (0, 0)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

            if dp[i][j] > max_side:
                max_side = dp[i][j]
                top_left = (i - max_side + 1, j - max_side + 1)

side, (row, col) = max_side, top_left

print(side)
print(row + 1, col + 1)
