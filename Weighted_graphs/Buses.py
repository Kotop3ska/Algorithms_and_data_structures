"""
Между некоторыми деревнями края Васюки ходят автобусы. 
Поскольку пассажиропотоки здесь не очень большие, то автобусы ходят всего несколько раз в день.

Марии Ивановне требуется добраться из деревни d в деревню v как можно быстрее 
(считается, что в момент времени 0 она находится в деревне d).

Входные данные
Сначала вводится число N – общее число деревень (1 <= N <= 100),  затем номера деревень d и v,  
за ними следует количество автобусных рейсов R (0 <= R <= 10000). Далее идут описания автобусных рейсов. 
Каждый рейс задается номером деревни отправления, временем отправления, деревней назначения и временем прибытия 
(все времена – целые от 0 до 10000). Если в момент t пассажир приезжает в какую-то деревню, 
то уехать из нее он может в любой момент времени, начиная с t.

Выходные данные
Выведите минимальное время, когда Мария Ивановна может оказаться в деревне v. 
Если она не сможет с помощью указанных автобусных рейсов добраться из d в v, выведите -1.
"""

import heapq


def dijkstra(graph, start, end, n):
    INF = float('inf')
    times = [INF] * (n + 1)
    times[start] = 0

    pq = [(0, start)]

    while pq:
        current_time, current_village = heapq.heappop(pq)

        if current_village == end:
            return current_time

        if current_time > times[current_village]:
            continue

        for dep_time, next_village, arr_time in graph[current_village]:
            if dep_time >= current_time:
                if arr_time < times[next_village]:
                    times[next_village] = arr_time
                    heapq.heappush(pq, (arr_time, next_village))

    return -1


N = int(input())
d, v = map(int, input().split())
R = int(input())

graph = {i: [] for i in range(1, N + 1)}

for _ in range(R):
    start, dep_time, end, arr_time = map(int, input().split())
    graph[start].append((dep_time, end, arr_time))

result = dijkstra(graph, d, v, N)
print(result)