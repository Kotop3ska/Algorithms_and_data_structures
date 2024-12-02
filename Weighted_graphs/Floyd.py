"""
Дан ориентированный граф, рёбрам которого приписаны некоторые неотрицательные веса (длины). 
Найти длину кратчайшего пути из вершины s в вершину t.

Входные данные
В первой строке заданы три числа: число вершин в графе N ≤50, номера вершин s и t. 
Далее идёт матрица смежности графа, то есть N строк, в каждой из которых записано N чисел. 
j-ое число в i-ой строке матрицы смежности задает длину ребра, ведущего из i-й вершину в j-ую. 
Длины могут принимать любые значения от 0 до 1000000, число -1 означает отсутствие соответствующего ребра. 
Гарантируется, что на главной диагонали матрицы стоят нули.

Выходные данные
Выведите одно число – минимальную длину пути. Если пути не существует, выведите -1.
"""

def floyd_marshall(graph, n, start, end):
    start -= 1
    end -= 1
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] != -1:
                dist[i][j] = graph[i][j]
            if i == j:
                dist[i][j] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist[start][end] if dist[start][end] != float('inf') else -1


n, start, end = map(int, input().split())
graph = [[int(i) for i in input().split()] for _ in range(n)]

print(floyd_marshall(graph, n, start, end))