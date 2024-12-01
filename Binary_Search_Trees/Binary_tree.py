"""
Напишите программу, которая будет реализовывать действия в бинарном дереве поиска «вставить», «удалить» и «найти» (по значению).
Программа должна обрабатывать запросы четырёх видов:

ADD n — если указанного числа еще нет в дереве, вставлять его и выводить слово «DONE», 
если уже есть — оставлять дерево как было и выводить слово «ALREADY».

DELETE n — если указанное число есть в дереве, удалять его и выводить слово «DONE», 
если нет — оставлять дерево как было и выводить слово «CANNOT». При удалении элемента, имеющего два сына, 
обязательно обменивать значение с максимальным элементом левого поддерева.

SEARCH — следует выводить слово «YES» (если значение найдено в дереве) или слово «NO» (если не найдено).
Дерево при этом не меняется.

PRINTTREE — выводить все дерево, обязательно используя алгоритм, указанный в формате вывода результатов.

Входные данные
В каждой строке входных данных записан один из запросов ADD n или DELETE n или SEARCH n или PRINTTREE. 
Гарантируется, что запросы PRINTTREE будут вызываться только в моменты, когда дерево не пустое. 
Общее количество запросов не превышает 1000, из них не более 20 запросов PRINTTREE.

Выходные данные
Для каждого запроса выводите ответ на него. Для запросов ADD, DELETE и SEARCH — соответствующее слово в отдельной строке.
"""

from sys import stdin


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.search(key):
            return False
        if self.root is None:
            self.root = Node(key)
        else:
            curr_node = self.root
            while True:
                if key < curr_node.data:
                    if curr_node.left is None:
                        curr_node.left = Node(key)
                        break
                    curr_node = curr_node.left
                elif key > curr_node.data:
                    if curr_node.right is None:
                        curr_node.right = Node(key)
                        break
                    curr_node = curr_node.right
                else:
                    break

    def height(self):
        return self._height_tree(self.root)

    def _height_tree(self, node):
        if node is None:
            return 0
        return 1 + max(self._height_tree(node.left), self._height_tree(node.right))

    def _max_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if node.data == key:
            return True
        if key < node.data:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.data:
            node.left = self._delete(node.left, key)
        elif key > node.data:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            max_node = self._max_node(node.left)
            node.data = max_node.data
            node.left = self._delete(node.left, max_node.data)
        return node

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    def print_tree(self, node, level):
        if node is None:
            return None
        self.print_tree(node.left, level + 1)
        for _ in range(level):
            print(".", end="")
        print(node.data)
        self.print_tree(node.right, level + 1)


if __name__ == "__main__":
    b_tree = BinarySearchTree()
    strings = stdin.readlines()
    for inp in strings:
        inp = inp.split()
        command = inp[0]
        if command == "ADD":
            num = int(inp[-1])
            if b_tree.search(num):
                print("ALREADY")
            else:
                b_tree.insert(num)
                print("DONE")
        elif command == "DELETE":
            num = int(inp[-1])
            if b_tree.search(num):
                b_tree.delete(num)
                print("DONE")
            else:
                print("CANNOT")
        elif command == "SEARCH":
            num = int(inp[-1])
            result = "YES" if b_tree.search(num) else "NO"
            print(result)
        elif command == "PRINTTREE":
            b_tree.print_tree(b_tree.root, 0)