from egz1btesty import runtests

def kstrong(T, k):
  n = len(T)
  memo = [[-1]*(k+1) for _ in range(n)]
  
  def f(i, s):
    if i == 0:
      return max(0, T[i])

    if memo[i][s] != -1:
      return memo[i][s]

    best = max(0, T[i], f(i-1, s) + T[i])
    if s > 0:
      best = max(f(i-1, s-1), best)

    memo[i][s] = best
    return best

  return max(f(i, k) for i in range(n))




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )
