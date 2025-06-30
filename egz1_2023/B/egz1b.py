from egz1btesty import runtests
from math import inf

def planets( D, C, T, E ):
    n = len(D)
    dp = [[inf]*(E+1) for _ in range(n)]

    for i in range(E+1):
        dp[0][i] = i*C[0]
    j, p = T[0]
    dp[j][0] = min(dp[0][0] + p, dp[j][0])

    for i in range(1, n):
        if (D[i]-D[i-1]) <= E:
            dp[i][0] = min(dp[i-1][(D[i] - D[i-1])], dp[i][0])
        j, p = T[i]
        dp[j][0] = min(dp[i][0] + p, dp[j][0])

        for tank in range(1, E+1):
            if tank + (D[i]-D[i-1]) <= E:
                dp[i][tank] = min(dp[i-1][tank+(D[i]-D[i-1])], dp[i][tank])
            dp[i][tank] = min(dp[i][tank-1] + C[i], dp[i][tank])

    return min(dp[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
