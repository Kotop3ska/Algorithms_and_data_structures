"""
Слово называется анаграммой другого слова, если оно может быть получено перестановкой его символов.

Входные данные
Даны два слова на отдельных строках. Слова состоят из строчных латинских букв и цифр. Длины слов не превышают 255.

Выходные данные
Требуется вывести "YES"  – если введенные слова являются анаграммами друг друга, "NO"  – если нет.

Примечание
Сложность работы программы должна быть O(n). 
Использование встроенной сортировки(sort, sorted), 
алгоритмов сортировки пузырёк/quick sort/merge sort и других запрещено!
"""

def check(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    if n1 != n2:
        return 'NO'
    d1 = {x: 0 for x in set(s1)}
    d2 = {x: 0 for x in set(s2)}
    for i in range(n1):
        d1[s1[i]] += 1
        d2[s2[i]] += 1
    if d1 == d2:
        return "YES"
    else:
        return "NO"


s1 = input()
s2 = input()
print(check(s1, s2))
