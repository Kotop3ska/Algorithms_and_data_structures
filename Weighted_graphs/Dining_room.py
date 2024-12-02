"""
Сегодня у студентов праздник! В одном из новых зданий университета решили открыть столовую. 
Для этих целей требуется выбрать одно из зданий, в котором и будет располагаться столовая. 
Чтобы студенты как можно меньше отвлекались от учёбы, было решено выбрать такое здание, 
чтобы максимальное расстояние от него до всех остальных зданий было как можно меньше.

Помогите найти такое здание!

Входные данные
В первой строке находятся два числе 𝑁 и 𝑀 - количество зданий и количество дорог, 
соединяющих здания (1≤𝑁≤100,0≤𝑀≤𝑁⋅(𝑁−1)/2). Далее в 𝑀 строках расположены описания дорог: 
3 целых числа 𝑠𝑖, 𝑒𝑖, 𝑙𝑖 - здания, в которых начинается и заканчивается дорога и длина дороги соответственно 
(1≤𝑠𝑖,𝑒𝑖≤𝑁,0≤𝑙𝑖≤100, дороги двунаправленные).

Выходные данные
Необходимо вывести одно число - номер искомого здания. 
Если есть несколько зданий удовлетворяющих поставленным критериям, выберите среди них здание с наименьшим номером.
"""

import heapq

INF = 2009000999


def dijkstra(graph, start, n):
    dist = [INF] * n
    dist[start] = 0


    pq = [(0, start)]

    while pq:
        cur_dist, cur_vertex = heapq.heappop(pq)

        if cur_dist > dist[cur_vertex]:
            continue

        for neighbor, weight in graph[cur_vertex].items():
            new_dist = cur_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist


n, m = map(int, input().split())
graph = {i: {} for i in range(n)}
for _ in range(m):
    frm, to, weight = map(int, input().split())
    frm -= 1
    to -= 1
    graph[frm][to] = weight
    graph[to][frm] = weight

min_max = [0] * n
for i in range(n):
    min_max[i] = max(dijkstra(graph, i, n))

print(min_max.index(min(min_max)) + 1)