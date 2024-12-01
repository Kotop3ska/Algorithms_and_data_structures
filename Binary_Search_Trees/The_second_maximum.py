"""
Выведите второй по величине элемент в построенном дереве. Гарантируется, что такой найдется.

Входные данные
Дана последовательность целых чисел, оканчивающаяся нулем. Сам ноль в последовательность не входит.

Выходные данные
Выведите ответ на задачу.
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
        return current.data

    def _second_max(self, node):
        previous = None
        current = node
        while current.right is not None:
            previous = current
            current = current.right
        if current.left:
            return self._max_node(current.left)
        return previous.data

    def second_max(self):
        return self._second_max(self.root)

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
    elements = list(map(int, stdin.read().split()))[:-1]  # Чтение данных из stdin и удаление последнего элемента
    for el in elements:
        b_tree.insert(el)

    print(b_tree.second_max())