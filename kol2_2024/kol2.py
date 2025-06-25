from kol2testy import runtests
from math import inf
from queue import PriorityQueue
from collections import deque

def dijkstra(G, s, t):
  n = len(G)
  dist = [[inf]*17 for _ in range(n)]
  Q = PriorityQueue()

  Q.put((0, s, 16))
  dist[s][16] = 0

  while not Q.empty():
    d, u, energy = Q.get()
    if d > dist[u][energy]:
      continue

    for v, g in G[u]:
      if g <= energy:
        if dist[v][energy-g] > dist[u][energy]+g:
          dist[v][energy - g] = dist[u][energy] + g
          Q.put((dist[v][energy - g], v, energy - g))
      else:
        if dist[v][16-g] > dist[u][energy]+g+8:
          dist[v][16 - g] = dist[u][energy] + g+8
          Q.put((dist[v][16 - g], v, 16 - g))

  return min(dist[t])

def turbo_bfs(G, s, t):
  n = len(G)
  dist = [[[inf]*17 for _ in range(17)] for _ in range(n)]
  Q = deque()

  dist[s][0][16] = 0
  Q.append((s, 0, 16))

  while Q:
    u, u_dist, energy = Q.popleft()

    if u_dist > 0:
      if dist[u][u_dist - 1][energy - 1] > dist[u][u_dist][energy] + 1:
        dist[u][u_dist - 1][energy - 1] = dist[u][u_dist][energy] + 1
        Q.append((u, u_dist - 1, energy - 1))
    else:
      for v, g in G[u]:
        if g <= energy:
          if dist[v][g - 1][energy - 1] > dist[u][0][energy] + 1:
            dist[v][g - 1][energy - 1] = dist[u][0][energy] + 1
            Q.append((v, g - 1, energy - 1))
        else:
          if dist[v][g - 1][15] > dist[u][0][energy] + 1 + 8:
            dist[v][g - 1][15] = dist[u][0][energy] + 1 + 8
            Q.append((v, g - 1, 15))

  return min(dist[t][0])

def warrior( G, s, t):
  n = max([max(u, v) for u, v, _ in G])+1
  graph = [[] for _ in range(n)]
  for u, v, w in G:
    graph[u].append((v, w))
    graph[v].append((u, w))

  # return dijkstra(graph, s, t) #ElogV
  return turbo_bfs(graph, s, t) #E + V

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )