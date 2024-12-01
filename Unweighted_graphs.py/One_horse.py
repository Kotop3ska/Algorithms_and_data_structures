"""
На шахматной доске NxN в клетке (x1, y1) стоит голодный шахматный конь. 
Он хочет попасть в клетку (x2, y2), где растет вкусная шахматная трава. 
Какое наименьшее количество ходов он должен для этого сделать?

Входные данные
На вход программы поступает  пять чисел: N, x1, y1, x2, y2 (5 <= N <= 20, 1 <= x1, y1, x2, y2 <= N). 
Левая верхняя клетка доски имеет координаты (1, 1), правая нижняя - (N, N).

Выходные данные
В первой строке выведите единственное число K - наименьшее необходимое число ходов коня. 
В каждой из следующих K+1 строк должно быть записано 2 числа - координаты очередной клетки в пути коня.
"""

from collections import deque

n = int(input())
(x1, y1) = map(int, input().split())
(x2, y2) = map(int, input().split())


def get_sit(x, y):
    directions = [
        (x - 2, y + 1),
        (x - 2, y - 1),
        (x + 2, y + 1),
        (x + 2, y - 1),
        (x + 1, y - 2),
        (x - 1, y - 2),
        (x + 1, y + 2),
        (x - 1, y + 2)
    ]
    sits = []
    for new_x, new_y in directions:
        if 1 <= new_x <= n and 1 <= new_y <= n:
            sits.append((new_x, new_y))
    return sits


def bfs(start, target):
    queue = deque([start])
    visited = {start}
    parents = {start: None}

    while queue:
        current = queue.popleft()

        if current == target:
            break

        for neighbor in get_sit(current[0], current[1]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                parents[neighbor] = current

    path = []
    step = target
    while step is not None:
        path.append(step)
        step = parents[step]
    path.reverse()
    return path


solution = bfs((x1, y1), (x2, y2))
print(len(solution) - 1)
for position in solution:
    print(*position)