"""
Реализуйте структуру данных "дек".  
Напишите программу, содержащую описание дека и моделирующую работу дека, реализовав все указанные здесь методы. 
Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. 
После выполнения каждой команды программа должна вывести одну строчку. Возможные команды для программы:

push_front
Добавить (положить) в начало дека новый элемент. Программа должна вывести ok.

push_back
Добавить (положить) в конец дека новый элемент. Программа должна вывести ok.

pop_front
Извлечь из дека первый элемент. Программа должна вывести его значение.

pop_back
Извлечь из дека последний элемент. Программа должна вывести его значение.

front
Узнать значение первого элемента (не удаляя его). Программа должна вывести его значение.

back
Узнать значение последнего элемента (не удаляя его). Программа должна вывести его значение.

size
Вывести количество элементов в деке.

clear
Очистить дек (удалить из него все элементы) и вывести ok.

exit
Программа должна вывести bye и завершить работу.
Гарантируется, что количество элементов в деке в любой момент не превосходит 100. 
Перед исполнением операций pop_front, pop_back, front, back программа должна проверять, 
содержится ли в деке хотя бы один элемент. Если во входных данных встречается операция pop_front, pop_back, front, back, 
и при этом дек пуст, то программа должна вместо числового значения вывести строку error.

Входные данные
Вводятся команды управления деком, по одной на строке.

Выходные данные
Требуется вывести протокол работы дека, по одному сообщению на строке
"""

class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push_front(self, item):
        self.items = [item] + self.items

    def push_back(self, item):
        self.items.append(item)

    def pop_front(self):
        if self.is_empty():
            return 'error'
        return self.items.pop(0)

    def pop_back(self):
        if self.is_empty():
            return 'error'
        return self.items.pop()

    def front(self):
        if self.is_empty():
            return 'error'
        return self.items[0]

    def back(self):
        if self.is_empty():
            return 'error'
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def exit(self):
        exit()


l = Deque()
command = [0, 0]
while command[0] != "exit":
    command = input().split()
    if command[0] == "pop_front":
        print(l.pop_front())
    elif command[0] == "front":
        print(l.front())
    elif command[0] == "pop_back":
        print(l.pop_back())
    elif command[0] == "back":
        print(l.back())
    elif command[0] == "size":
        print(l.size())
    elif command[0] == "clear":
        l.clear()
        print("ok")
    elif command[0] == "push_front":
        n = int(command[1])
        l.push_front(n)
        print("ok")
    elif command[0] == 'push_back':
        n = int(command[1])
        l.push_back(n)
        print("ok")
    else:
        print("bye")
        l.exit()

