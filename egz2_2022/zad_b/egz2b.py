from egz2btesty import runtests
from math import inf

def magic( C ):
    n = len(C)
    dp = [-inf]*n
    dp[0] = 0

    for i in range(n):
        gold, d0, d1, d2 = C[i]

        for cost, j in [d0, d1, d2]:
            if j > i and dp[i] + gold >= cost and gold - cost <= 10:
                dp[j] = max(dp[j], dp[i] + gold - cost)

    return max(dp[n-1], -1)

from egz2btesty import runtests

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
