"""
Дан ориентированный взвешенный граф. Найдите кратчайший путь от одной заданной вершины до другой.

Входные данные
В первой строке содержатся три числа: N, S и F (1≤N≤100, 1≤S, F≤N), 
где N – количество вершин графа, S – начальная вершина, а F – конечная. 
В следующих N строках вводится по N чисел, не превосходящих 100, – матрица смежности графа, 
где -1 означает отсутствие ребра между вершинами, а любое неотрицательное число – присутствие ребра данного веса. 
На главной диагонали матрицы записаны нули.

Выходные данные
Требуется вывести последовательно все вершины одного (любого) из кратчайших путей, или одно число -1, 
если пути между указанными вершинами не существует. В ответе примера указано количество вершин, а не сам путь. 
Ваша программа должна выдавать именно путь.
"""

def dijkstra(graph, start, end):
    start -= 1
    end -= 1
    n = len(graph)
    prev = [-1] * n
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
                    prev[i] = min_index

    if dist[end] == float('inf'):
        print(-1)
    else:
        curr = end
        ans = [curr + 1]
        while prev[curr] + 1 > 0:
            curr = prev[curr]
            ans.append(curr + 1)
        print(*ans[::-1])


n, start, end = map(int, input().split())

graph = [[int(i) for i in input().split()] for _ in range(n)]
dijkstra(graph, start, end)