"""
Рассмотрим последовательность целых чисел длины N. 
По ней с шагом 1 двигается “окно” длины K, то есть сначала в “окне” видно первые K чисел, 
на следующем шаге в “окне” уже будут находиться K чисел, начиная со второго, и так далее до конца последовательности. 
Требуется для каждого положения “окна” определить минимум в нём.

Входные данные
В первой строке входных данных содержатся два числа N и K (1 ≤  N ≤  150000, 1 ≤ K ≤ 10000, K ≤  N) – 
длины последовательности и “окна”, соответственно. На следующей строке находятся N чисел – сама последовательность.

Выходные данные
Выходые данные должны содержать N − K + 1 строк – минимумы для каждого положения “окна”.
"""

N, K = map(int, input().split())
seq = list(map(int, input().split()))

L = []
for i in range(N):
    while L and L[0] <= i - K:
        L.pop(0)

    while L and seq[L[-1]] > seq[i]:
        L.pop()

    L.append(i)

    if i >= K - 1:
        print(seq[L[0]])