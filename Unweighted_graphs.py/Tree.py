"""
Имеется неориентированный граф, состоящий из N вершин и M ребер. Необходимо проверить, является ли граф деревом. 
Напомним, что дерево — это связный граф, в котором нет циклов 
(следовательно, между любой парой вершин существует ровно один простой путь). 
Граф называется связным, если от одной вершины существует путь до любой другой.

Входные данные
Во входном файле в первой строке содержатся два целых числа N и M (1 ≤ N ≤ 100, 0 ≤ M ≤ 1000), записанные через пробел. 
Далее следуют M различных строк с описаниями ребер, каждая из которых содержит два натуральных числа Ai и 
Bi (1 ≤ Ai <Bi ≤ N), где Ai и Bi — номера вершин, соединенных i-м ребром.

Выходные данные
В выходной файл выведите слово YES, если граф является деревом или NO в противном случае.
"""

n, m = map(int, input().split())
graph = {x: [] for x in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)


def dfs_for_loop(v, parent):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            if dfs_for_loop(u, v):
                return True
        elif u != parent:
            return True
    return False


def is_loop():
    for key in graph:
        if not visited[key]:
            if dfs_for_loop(key, -1):
                return True
    return False


def dfs_for_connect(v, vis):
    vis.add(v)
    for u in graph[v]:
        if u not in vis:
            dfs_for_connect(u, vis)


def is_connected():
    vis = set()
    dfs_for_connect(1, vis)
    return len(vis) == n


def is_tree():
    if is_loop():
        return False
    return is_connected()


if is_tree():
    print('YES')
else:
    print('NO')