from egz3atesty import runtests
from collections import deque

def mykoryza( G,T,d ):
  n = len(G)
  mushrooms = [-1]*n

  q = deque()
  for i in range(len(T)):
    mushrooms[T[i]] = i
    q.append(T[i])

  while q:
    u = q.popleft()
    for v in G[u]:
      if mushrooms[v] == -1:
        mushrooms[v] = mushrooms[u]
        q.append(v)

  return mushrooms.count(d)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )
