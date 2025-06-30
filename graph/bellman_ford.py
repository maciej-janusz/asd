# O(VE)
from math import inf

def bellman_ford(edges, n, s):
    dist = [inf] * n
    dist[s] = 0

    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None

    return dist
