"""
Дано N золотых слитков массой m1, …, mN. Ими наполняют рюкзак, который выдерживает вес не более M.
Какую наибольшую массу золота можно унести в таком рюкзаке?

Входные данные
В первой строке вводится натуральное число N, не превышающее 100 и натуральное число M, не превышающее 10000.

Во второй строке вводятся N натуральных чисел mi, не превышающих 100.

Выходные данные
Выведите одно целое число - наибольшую возможную массу золота, которую можно унести в данном рюкзаке.
"""


def backpack(v, W):
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]
            if v[i] <= w and dp[i - 1][w - v[i]]:
                dp[i][w] = 1
    return max(w for w in range(W + 1) if dp[n][w] == 1)


n, M = map(int, input().split())
massa = [0] + list(map(int, input().split()))
max_massa = backpack(massa, M)
print(max_massa)