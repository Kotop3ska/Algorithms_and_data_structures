"""
Выведите все исходные точки в порядке возрастания их расстояний от начала координат. 
Создайте структуру Point и сохраните исходные данные в массиве структур Point.

Входные данные
Программа получает на вход набор точек на плоскости. 
Сначала задано количество точек n, затем идет последовательность из n строк, 
каждая из которых содержит два числа: координаты точки.
Величина n не превосходит 100, все исходные координаты – целые числа, не превосходящие 103.

Выходные данные
Необходимо вывести  все исходные точки в порядке возрастания их расстояний от начала координат. 
Программа выводит только координаты точек, их количество выводить не надо.
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return self.x ** 2 + self.y ** 2


def bubble_sort(points, n):
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if points[j].distance() > points[j + 1].distance():
                points[j], points[j + 1], = points[j + 1], points[j]
                swapped = True
        if not swapped:
            break
    return points


n = int(input())
points = []

for i in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))

bubble_sort(points, n)

for point in points:
    print(point.x, point.y)