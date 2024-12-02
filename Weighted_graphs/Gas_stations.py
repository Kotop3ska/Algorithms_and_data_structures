"""
В стране N городов, некоторые из которых соединены между собой дорогами. 
Для того, чтобы проехать по одной дороге, требуется один бак бензина. 
В каждом городе бак бензина имеет разную стоимость. 
Вам требуется добраться из первого города в N-ый, потратив как можно меньшее денег. Покупать бензин впрок нельзя.

Входные данные
В первой строке вводится число N (1≤N≤100), в следующей строке идет N чисел, 
i-ое из которых задает стоимость бензина в i-ом городе (всё это целые числа из диапазона от 0 до 100). 
Затем идет число M – количество дорог в стране, далее идет описание самих дорог. 
Каждая дорога задается двумя числами – номерами городов, которые она соединяет. 
Все дороги двухсторонние (то есть по ним можно ездить как в одну, так и в другую сторону), 
между двумя городами всегда существует не более одной дороги, не существует дорог, ведущих из города в себя.

Выходные данные
Требуется вывести одно число – суммарную стоимость маршрута или -1, если добраться невозможно.
"""

def dijkstra(graph, start, end, cost):
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
        ans_cost = []
        for i in ans[::-1]:
            ans_cost.append(cost[i - 1])
        print(sum(ans_cost[:-1]))


def matr_weight(data, n, cost):
    matrix = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 0

    for a, b in data:
        matrix[a - 1][b - 1] = cost[b - 1]
        matrix[b - 1][a - 1] = cost[a - 1]
    return matrix


n = int(input())
cost = [int(x) for x in input().split()]
m = int(input())
start = 1
end = n
data = [set(map(int, input().split())) for _ in range(m)]
graph = matr_weight(data, n, cost)
dijkstra(graph, start, end, cost)
