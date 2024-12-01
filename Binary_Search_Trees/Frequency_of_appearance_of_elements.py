"""
По данной последовательности постройте дерево, 
запоминая для каждого элемента его значение и количество его повторений в последовательности.

Входные данные
Вводится последовательность целых чисел, заканчивающаяся нулем.
Сам ноль в последовательность не входит.

Выходные данные
Выведите на экран содержимое дерева в порядке возрастания, по одному элементу на строку. 
В каждой строке выводите значение элемента, затем, через пробел, укажите, 
сколько раз он встречается в исходной последовательности.
"""

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.count = 1


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
                    curr_node.count += 1
                    break

    def in_order_traversal(self):
        self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if node is None:
            return
        self._in_order_traversal(node.left)
        print(node.data, node.count)
        self._in_order_traversal(node.right)

    def get_leaves(self):
        self._get_leaves(self.root)

    def _get_leaves(self, node):
        if node is None:
            return
        self._get_leaves(node.left)
        if not node.right and not node.left:
            print(node.data)
        self._get_leaves(node.right)

    def height(self):
        return self._height_tree(self.root)

    def _height_tree(self, node):
        if node is None:
            return 0
        return 1 + max(self._height_tree(node.left), self._height_tree(node.right))

    def is_balanced(self):
        return self._is_balanced(self.root)

    def _is_balanced(self, node):
        if node is None:
            return True, 0
        left_balanced, left_height = self._is_balanced(node.left)
        right_balanced, right_height = self._is_balanced(node.right)

        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        height = 1 + max(left_height, right_height)

        return balanced, height


if __name__ == "__main__":
    bst = BinarySearchTree()
    numbers = list(map(int, input().split()))

    for number in numbers:
        if number == 0:
            break
        bst.insert(number)

    bst.in_order_traversal()