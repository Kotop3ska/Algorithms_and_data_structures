"""
В неориентированном графе требуется найти минимальный путь между двумя вершинами.

Входные данные
Первым на вход поступает число N – количество вершин в графе (1 ≤ N ≤ 100). 
Затем записана матрица смежности (0 обозначает отсутствие ребра, 1 – наличие ребра). 
Далее задаются номера двух вершин – начальной и конечной.

Выходные данные
Выведите сначала L – длину кратчайшего пути (количество ребер, которые нужно пройти), а потом сам путь. 
Если путь имеет длину 0, то его выводить не нужно, достаточно вывести длину.

Необходимо вывести путь (номера всех вершин в правильном порядке). Если пути нет, нужно вывести -1.
"""

from collections import deque

n = int(input())

graph = {i: set() for i in range(n)}
for i in range(n):
    edge = list(map(int, input().split()))
    for j in range(n):
        if edge[j] == 1:
            graph[j].add(i)

s, t = map(int, input().split())
s -= 1
t -= 1

INF = 1e9
dist = [INF] * (n + 1)
dist[s] = 0
q = deque([s])
pred = [-1] * n

while q:
    node = q.popleft()
    for neighbor in graph[node]:
        if dist[neighbor] == INF:
            dist[neighbor] = dist[node] + 1
            pred[neighbor] = node
            q.append(neighbor)

if s == t:
    print(0)
elif dist[t] != INF:
    print(dist[t])
    path = [t]
    ver = pred[t]
    while ver != -1:
        path.append(ver)
        ver = pred[ver]

    print(*[x + 1 for x in path[::-1]])
else:
    print(-1)