"""
Дан ориентированный граф. Требуется определить, есть ли в нем цикл.

Входные данные
В первой строке вводится число вершин N≤ 50. Далее в N строках следуют по N чисел, каждое из которых – 0 или 1. 
j-ое число в i-ой строке равно 1 тогда и только тогда, когда существует ребро, идущее из i-ой вершины в j-ую. 
Гарантируется, что на диагонали матрицы будут стоять нули.

Выходные данные
Выведите 0, если в заданном графе цикла нет, и 1, если он есть.
"""

n = int(input())
graph = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    graph.append(row)
visited = [0] * n


def dfs(v):
    visited[v] = 1
    for u in range(n):
        if graph[v][u] == 1:
            if visited[u] == 0:
                if dfs(u):
                    return True
            elif visited[u] == 1:
                return True
    visited[v] = 2
    return False


flag = False
for v in range(n):
    if visited[v] == 0:
        if dfs(v):
            flag = True
            break

if flag:
    print(1)
else:
    print(0)
