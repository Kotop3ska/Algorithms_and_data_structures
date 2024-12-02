"""
Дан ориентированный взвешенный граф. Найдите кратчайшее расстояние от одной заданной вершины до другой.

Входные данные
В первой строке содержатся три числа: N, S и F (1≤ N≤ 100, 1≤ S, F≤ N), где N – количество вершин графа, 
S – начальная вершина, а F – конечная. В следующих N строках вводится по N чисел, 
не превосходящих 100, – матрица смежности графа, где -1 означает отсутствие ребра между вершинами, 
а любое неотрицательное число – присутствие ребра данного веса. На главной диагонали матрицы записаны нули.

Выходные данные
Требуется вывести искомое расстояние или -1, если пути между указанными вершинами не существует.
"""

n, s, f = map(int, input().split())
graph = [[int(x) for x in input().split()] for _ in range(n)]
s -= 1
f -= 1


def dijkstra(graph, start, end):
    n = len(graph)
    visited = [False] * n
    dist = [float('inf')] * n
    dist[start] = 0

    for _ in range(n):
        min_dist = float('inf')
        min_index = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_index = i

        if min_index == -1:
            break

        visited[min_index] = True
        for i in range(n):
            if graph[min_index][i] >= 0:
                new_dist = dist[min_index] + graph[min_index][i]
                if new_dist < dist[i]:
                    dist[i] = new_dist

    return dist[end] if dist[end] != float('inf') else -1


print(dijkstra(graph, s, f))