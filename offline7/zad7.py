from zad7testy import runtests
from math import inf

def orchard(T, m):
    n = len(T)
    dp = [[inf]*m for _ in range(n)]

    dp[0][0] = 1
    for k in range(m):
        if T[0]%m == k:
            dp[0][k] = 0

    for i in range(1, n):
        for k in range(m):
            dp[i][k] = min(inf, dp[i-1][(k-T[i])%m], dp[i-1][k]+1)

    return dp[-1][0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
