from zad6testy import runtests
from math import inf



def parking(X,Y):
  memo = {}

  def f(i, j):
    if (i, j) in memo:
      return memo[(i, j)]

    if i == 0 and j == 0:
      result = abs(X[i]-Y[j])
    elif i > 0 and j == 0:
      result = inf
    elif i == 0 and j > 0:
      result = min(abs(X[i]-Y[j]), f(i, j-1))
    else:
      result = min(f(i, j-1), f(i-1, j-1) + abs(X[i]-Y[j]))
    memo[(i, j)] = result
    return result

  return f(len(X)-1, len(Y)-1)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
