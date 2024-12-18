"""
Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных скобок. 
Программа дожна определить, является ли данная скобочная последовательность правильной.

Пустая последовательность явлется правильной. Если A – правильная, то последовательности (A), [A], {A} – правильные. 
Если A и B – правильные последовательности, то последовательность AB – правильная.

Входные данные
В единственной строке записана скобочная последовательность, содержащая не более 100000 скобок.

Выходные данные
Если данная последовательность правильная, то программа должна вывести строку yes, иначе строку no.
"""

s = input()
stack = []
ans = True

for item in s:
    if item not in ['(', '{', '[', ')', '}', ']']:
        continue
    if item in ['(', '{', '[']:
        stack.append(item)
        continue
    if len(stack) != 0 and (item == ')' and stack[-1] == '(' or
                            item == '}' and stack[-1] == '{' or
                            item == ']' and stack[-1] == '['):
        stack.pop()
    else:
        ans = False
        break

if len(stack) != 0:
    ans = False

print('yes' if ans else 'no')