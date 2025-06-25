from zad9testy import runtests
from math import inf

def trip(M):
  m = len(M)
  n = len(M[0])

  order = sorted([(M[i][j], i, j) for i in range(m) for j in range(n)])
  dp = [[0]*m for _ in range(n)]
  res = 0

  for i in range(n*m-1, -1, -1):
    _, x1, y1 = order[i]
    best = 1
    if x1 > 0:
      best = max(dp[y1][x1-1]+1, best)
    if x1 < m-1:
      best = max(dp[y1][x1+1]+1, best)
    if y1 > 0:
      best = max(dp[y1-1][x1]+1, best)
    if y1 < n-1:
      best = max(dp[y1+1][x1]+1, best)

    res = max(res, best)
    dp[y1][x1] = best

  return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )