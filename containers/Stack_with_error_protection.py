"""
Реализуйте структуру данных "стек". Напишите программу, содержащую описание стека и моделирующую работу стека, 
реализовав все указанные здесь методы. 
Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. 
После выполнения каждой команды программа должна вывести одну строчку. Возможные команды для программы:
push n
Добавить в стек число n (значение n задается после команды). Программа должна вывести ok. 
pop
Удалить из стека последний элемент. Программа должна вывести его значение. 
back
Программа должна вывести значение последнего элемента, не удаляя его из стека. 
size
Программа должна вывести количество элементов в стеке. 
clear
Программа должна очистить стек и вывести ok. 
exit
Программа должна вывести bye и завершить работу.
Перед исполнением операций back и pop программа должна проверять, содержится ли в стеке хотя бы один элемент. 
Если во входных данных встречается операция back или pop, и при этом стек пуст, 
то программа должна вместо числового значения вывести строку error.
Входные данные
Вводятся команды управления стеком, по одной на строке
Выходные данные
Программа должна вывести протокол работы стека, по одному сообщению на строке
"""

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        print('ok')
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print('error')
        else:
            print(self.items.pop())

    def back(self):
        if self.is_empty():
            print("error")
        else:
            print(self.items[-1])

    def size(self):
        print(len(self.items))

    def clear(self):
        self.items = []
        print('ok')

    def exit(self):
        print('bye')
        exit()


l = Stack()
cmmnds = []
command = [0, 0]
while command[0] != 'exit':
    command = input().split()
    cmmnds.append(command)

for command in cmmnds:
    if command[0] == 'push':
        l.push(command[1])
    elif command[0] == 'pop':
        l.pop()
    elif command[0] == 'back':
        l.back()
    elif command[0] == 'size':
        l.size()
    elif command[0] == 'clear':
        l.clear()
    elif command[0] == 'exit':
        l.exit()
