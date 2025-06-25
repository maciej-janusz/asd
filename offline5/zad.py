from zadtesty import runtests
from math import inf

def goodknight( G, s, t ):
  max_energy = 16
  n = len(G)
  visited = [[False]*(max_energy+1) for _ in range(n)]
  dist = [[inf]*(max_energy+1) for _ in range(n)]
  dist[s][max_energy] = 0

  while True:
    mini = inf
    u = -1
    energy = -1
    for v in range(n):
      for e in range(max_energy, -1, -1):
        if not visited[v][e] and dist[v][e] < mini:
          u = v
          energy = e
          mini = dist[v][e]

    if u == -1:
      break

    visited[u][energy] = True
    for v in range(n):
      if G[u][v] > 0:
        if G[u][v] > energy:
          if dist[v][max_energy-G[u][v]] > dist[u][energy] + G[u][v] + 8:
            dist[v][max_energy-G[u][v]] = dist[u][energy] + G[u][v] + 8
        else:
          if dist[v][energy - G[u][v]] > dist[u][energy] + G[u][v]:
            dist[v][energy - G[u][v]] = dist[u][energy] + G[u][v]

  return min(dist[t])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )
