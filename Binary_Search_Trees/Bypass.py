"""
Выведите все элементы полученного дерева в порядке возрастания.

Входные данные
Вводится последовательность целых чисел, оканчивающаяся нулем. Сам ноль в последовательность не входит. По данной последовательности требуется построить дерево.

Выходные данные
Выведите ответ на задачу.
"""

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
                        break
                    curr_node = curr_node.right
                else:
                    break

    def in_order_traversal(self):
        self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if node is None:
            return
        self._in_order_traversal(node.left)
        print(node.data) 
        self._in_order_traversal(node.right)

    def height(self):
        return self._height_tree(self.root)

    def _height_tree(self, node):
        if node is None:
            return 0
        return 1 + max(self._height_tree(node.left), self._height_tree(node.right))

    def _min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.data

    def min_node(self):
        return self._min_node(self.root)

    def _max_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.data

    def max_node(self):
        return self._max_node(self.root)

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)


if __name__ == "__main__":
    bst = BinarySearchTree()
    numbers = list(map(int, input().split()))

    for number in numbers:
        if number == 0:
            break
        bst.insert(number)

    bst.in_order_traversal()