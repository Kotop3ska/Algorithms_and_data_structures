"""
В постфиксной записи (или обратной польской записи) операция записывается после двух операндов. 
Например, сумма двух чисел A и B записывается как A B +. Запись B C + D * обозначает привычное нам (B + C) * D, 
а запись A B C + D * + означает A + (B + C) * D. Достоинство постфиксной записи в том, 
что она не требует скобок и дополнительных соглашений о приоритете операторов для своего чтения.

Входные данные
В единственной строке записано выражение в постфиксной записи, содержащее цифры и операции +, -, *. 
Цифры и операции разделяются пробелами. В конце строки может быть произвольное количество пробелов.

Выходные данные
Необходимо вывести значение записанного выражения.
"""

ls = input().split()
stack = []
for c in ls:
    if not c.isnumeric():
        b = stack.pop()
        a = stack.pop()
        if c == '+':
            res = a + b
        if c == '-':
            res = a - b
        if c == '*':
            res = a * b
        stack.append(res)
    else:
        stack.append(int(c))
print(stack[0])