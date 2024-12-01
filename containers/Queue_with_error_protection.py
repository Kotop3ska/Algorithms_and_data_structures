"""
Реализуйте структуру данных "очередь".
Напишите программу, содержащую описание очереди и моделирующую работу очереди, реализовав все указанные здесь методы.  
Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. 
После выполнения каждой команды программа должна вывести одну строчку. Возможные команды для программы:

push n
Добавить в очередь число n (значение n задается после команды). Программа должна вывести ok. 
pop
Удалить из очереди первый элемент. Программа должна вывести его значение. 
front
Программа должна вывести значение первого элемента, не удаляя его из очереди. 
size
Программа должна вывести количество элементов в очереди. 
clear
Программа должна очистить очередь и вывести ok. 
exit
Программа должна вывести bye и завершить работу.
Перед исполнением операций front и pop программа должна проверять, содержится ли в очереди хотя бы один элемент. 
Если во входных данных встречается операция front или pop, и при этом очередь пуста, 
то программа должна вместо числового значения вывести строку error.

Входные данные
Вводятся команды управления очередью, по одной на строке

Выходные данные
Требуется вывести протокол работы очереди, по одному сообщению на строке
"""

class Queue:
    def __init__(self):
        self.right = []
        self.left = []

    def size(self):
        return len(self.left) + len(self.right)

    def push(self, item):
        self.left.append(item)

    def is_empty(self):
        if (len(self.left) + len(self.right)) == 0:
            return 1
        else:
            return 0

    def pop(self):
        if self.is_empty():
            return "error"
        if len(self.right) == 0:
            while len(self.left) != 0:
                self.right.append(self.left.pop())
        return self.right.pop()

    def front(self):
        if self.is_empty():
            return "error"
        if len(self.right) == 0:
            while len(self.left) != 0:
                self.right.append(self.left.pop())
        return self.right[-1]

    def clear(self):
        self.right = []
        self.left = []

queue = Queue()
command = input()
while command != "exit":
    if command == "pop":
        print(queue.pop())
    elif command == "front":
        print(queue.front())
    elif command == "size":
        print(queue.size())
    elif command == "clear":
        queue.clear()
        print("ok")
    else:
        n = int(command[4::])
        queue.push(n)
        print("ok")
    command = input()
print("bye")