"""
Идёт 2163 год. Мишу, который работает в отделении таможни при космодроме города Нью-Питер, вызвал в кабинет шеф.

Как оказалось, недавно Министерство Налогов и Сборов выделило отделению определённую сумму денег на установку новых аппаратов 
для автоматического досмотра грузов. Естественно, средства были выделены с таким расчётом, чтобы грузы теперь находились 
на таможне ровно столько времени, сколько требуется непосредственно на их досмотр.

В руках шефа каким-то образом оказались сведения о надвигающейся ревизии – список из 𝑁 грузов, 
которые будут контролироваться Министерством. Для каждого груза известны время его прибытия, 
отсчитываемое с некоторого момента, хранимого в большом секрете, и время, требуемое аппарату для обработки этого груза. 
Шеф дал Мише задание по этим данным определить, какое минимальное количество аппаратов необходимо заказать на заводе, 
чтобы все грузы Министерства начинали досматриваться сразу после прибытия. Необходимо учесть, что конструкция тех аппаратов,
которые было решено установить, не позволяет обрабатывать два груза одновременно на одном аппарате. Напишите программу, 
которая поможет Мише справиться с его задачей.

Входные данные
На первой строке входного файла задано число 𝑁 (0 ≤ 𝑁 ≤ 50 000). 
На следующих 𝑁 строках находится по 2 целых положительных числа 𝑇𝑖 и 𝐿𝑖 – время прибытия соответствующего груза и время, т
ребуемое для его обработки (1 ≤ 𝑇𝑖 ≤ 106, 1 ≤ 𝐿𝑖 ≤ 10^6).

Выходные данные
В выходной файл выведите одно число – наименьшее количество аппаратов, которое нужно установить, 
чтобы не вызвать подозрений у Министерства.
"""

import heapq

n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

times.sort()
h = []

for t, l in times:
    if h and h[0] <= t:
        heapq.heappop(h)
    heapq.heappush(h, t + l)

print(len(h))