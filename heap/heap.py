"""
В этой задаче вам необходимо организовать структуру данных Heap для хранения целых чисел, 
над которой определены следующие операции:

   a) Insert(k) – добавить в Heap число k (1 ≤  k ≤ 1000000) ;
   b) Extract достать из Heap наибольшее число (удалив его при этом).

Входные данные
В первой строке содержится количество команд N (1 ≤  N ≤ 100000), далее следуют N команд, каждая в своей строке. 
Команда может иметь  формат: “0 <число>” или “1”, обозначающий, соответственно, операции Insert(<число>) и Extract. 
Гарантируется, что при выполенении команды Extract в структуре находится по крайней мере один элемент.

Выходные данные
Для каждой команды извлечения необходимо отдельной строкой вывести число, полученное при выполнении команды Extract.
"""

class MaxHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def shiftUp(self, i):
        while i // 2 > 0 and self.heap[i] > self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.shiftUp(self.size)

    def shiftDown(self, i):
        while i * 2 <= self.size:
            j = self.indMaxChild(i)
            if self.heap[i] < self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def indMaxChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        if self.heap[i * 2] > self.heap[i * 2 + 1]:
            return i * 2
        return i * 2 + 1

    def delMax(self):
        if self.size == 0:
            return None
        removed = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.shiftDown(1)
        return removed

    def getMax(self):
        if self.size == 0:
            return None
        return self.heap[1]


heap = MaxHeap()
n = int(input())
for _ in range(n):
    com = [int(x) for x in input().split()]
    if com[0] == 0:
        heap.insert(com[1])
    else:
        print(heap.delMax())
