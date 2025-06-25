"""
    albo tankujemy do pelna albo nie tankujemy
"""
from math import inf

def truck(L, pos, price):
    n = len(pos)
    dp = [[inf]*(L+1) for _ in range(n)]

    dp[0][L] = price[0]*L

    for i in range(1, n):
        d = pos[i] - pos[i-1]
        for s in range(L+1-d):
            dp[i][s] = min(dp[i][s], dp[i-1][s+d])
            dp[i][L] = min(dp[i][L], dp[i][s] + price[i]*(L-s))

    return min(dp[n-1])


L = 50
pos = [0, 20, 40, 60, 70]
price = [7, 3, 2, 5, 10]

print(truck(L, pos, price))
