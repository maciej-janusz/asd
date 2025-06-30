from egz1Atesty import runtests
from queue import PriorityQueue
from math import inf

def dijkstra(G, s, mult, r):
  n = len(G)
  costs = [inf]*n

  Q = PriorityQueue()
  costs[s] = 0
  Q.put((0, s))

  while not Q.empty():
    d, u = Q.get()
    if costs[u] < d:
      continue

    for v, cost in G[u]:
      if costs[u] + cost*mult + r < costs[v]:
        costs[v] = costs[u] + cost*mult + r
        Q.put((costs[v], v))

  return costs

def gold(G,V,s,t,r):
  n = len(G)
  cost_from_start = dijkstra(G, s, 1, 0)
  cost_from_end = dijkstra(G, t, 2, r)

  best = inf
  for i in range(n):
    best = min(best, cost_from_start[i] + cost_from_end[i] - V[i])
  return best


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
