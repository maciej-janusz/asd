from egz1atesty import runtests
from math import inf
from queue import PriorityQueue


def dijkstra(graph, s):
  n = len(graph)
  dists = [inf] * n

  Q = PriorityQueue()
  dists[s] = 0
  Q.put((0, s))

  while not Q.empty():
    d, u = Q.get()
    if d > dists[u]:
      continue

    for v, w in graph[u]:
      if dists[u] + w < dists[v]:
        dists[v] = dists[u] + w
        Q.put((dists[v], v))

  return dists


def armstrong( B, G, s, t):
  n = 0
  for u, v, w in G:
    n = max(n, u+1, v+1)

  graph = [[] for _ in range(n)]
  for u, v, w in G:
    graph[u].append((v, w))
    graph[v].append((u, w))

  bikes = [inf]*n
  for i, p, q in B:
    mult = p/q
    bikes[i] = min(mult, bikes[i])

  dist_to = dijkstra(graph, s)
  dist_from = dijkstra(graph, t)

  best = dist_to[t]
  for i in range(n):
    best = min(best, dist_to[i]+bikes[i]*dist_from[i])

  return int(best)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
