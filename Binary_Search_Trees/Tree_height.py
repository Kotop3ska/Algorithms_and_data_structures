"""
Реализуйте бинарное дерево поиска для целых чисел. 
Программа получает на вход последовательность целых чисел и строит из них дерево. 
Элементы в деревья добавляются в соответствии с результатом поиска их места. 
Если элемент уже существует в дереве, добавлять его не надо. Балансировка дерева не производится.

Входные данные
На вход программа получает последовательность натуральных чисел. 
Последовательность завершается числом 0, которое означает конец ввода, и добавлять его в дерево не надо.

Выходные данные
Выведите единственное число – высоту получившегося дерева.
"""

from random import randint
import queue


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
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
                    curr_node = curr_node.right
                else:
                    break

    def height(self):
        return self._height_tree(self.root)

    def _height_tree(self, node):
        if node is None:
            return 0
        return 1 + max(self._height_tree(node.left), self._height_tree(node.right))


if __name__ == "__main__":
    bst = BinarySearchTree()
    numbers = [int(x) for x in input().split()][:-1]
    for number in numbers:
        bst.insert(number)
    print(bst.height())