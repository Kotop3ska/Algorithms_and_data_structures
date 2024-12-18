"""
Напомним, что вершина ориентированного графа называется истоком, если в нее не входит ни одно ребро и стоком, 
если из нее не выходит ни одного ребра.

Ориентированный граф задан матрицей смежности. Найдите все вершины графа, которые являются истоками, 
и все его вершины, которые являются стоками.

Входные данные
Сначала вводится число n ( 1≤𝑛≤100 ) – количество вершин в графе, а затем n строк по n чисел, 
каждое из которых равно 0 или 1, – его матрица смежности.

Выходные данные
Вначале выведите k – число истоков в графе и затем k чисел – номера вершин, которые являются истоками, 
в возрастающем порядке. Затем выведите информацию о стоках в том же порядке.
"""

n = int(input())
matrix = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

ist = []
st = []

for i in range(n):
    flag_ist = True
    flag_st = True
    for j in range(n):
        if matrix[j][i] != 0:
            flag_ist = False
        if matrix[i][j] != 0:
            flag_st = False

    if flag_ist:
        ist.append(i + 1)
    if flag_st:
        st.append(i + 1)


print(len(ist))
for i in range(len(ist)):
    print(ist[i])
print(len(st))
for i in range(len(st)):
    print(st[i])