"""
Дан неориентированный невзвешенный граф. Необходимо посчитать количество его компонент связности и вывести их.

Входные данные
Во входном файле записано два числа 𝑁 и 𝑀 (0 < 𝑁 ≤ 100000, 0 ≤ 𝑀 ≤ 100000). 
В следующих 𝑀 строках записаны по два числа 𝑖 и 𝑗 (1 ≤ 𝑖, 𝑗 ≤ 𝑁), которые означают, что вершины 𝑖 и 𝑗 соединены ребром.

Выходные данные
В первой строчке выходного файла выведите количество компонент связности. 
Далее выведите сами компоненты связности в следующем формате: в первой строке количество вершин в компоненте, 
во второй - сами вершины в произвольном порядке.
"""

import sys
sys.setrecursionlimit(200000)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
components = []


def dfs(v, component):
    visited[v] = True
    component.append(v)
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, component)


for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


for vertex in range(1, n + 1):
    if not visited[vertex]:
        component = []
        dfs(vertex, component)
        components.append(component)

print(len(components))
for component in components:
    print(len(component))
    print(*component)