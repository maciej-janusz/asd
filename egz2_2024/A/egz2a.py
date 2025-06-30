from egz2atesty import runtests
from math import inf

def wired( T ):
  n = len(T)
  memo = [[inf]*n for _ in range(n)]
  def f(i, j):
    if j - i % 2 == 0:
      return inf
    if i > j:
      return 0
    if memo[i][j] < inf:
      return memo[i][j]


    best = inf
    for k in range(i+1, j+1, 2):
      best = min(best, abs(T[i] - T[k]) + 1 + f(i+1, k-1) + f(k+1, j))

    memo[i][j] = best
    return best

  return f(0, n-1)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wired, all_tests = True )
