from zad4testy import runtests
from queue import PriorityQueue
from math import inf


def relax(G, u, v, g, dist):
    if dist[u] + g < dist[v]:
        dist[v] = dist[u] + g
        return True
    return False
def dijkstra(G, s, t):
    n = len(G)
    dist = [inf] * n

    Q = PriorityQueue()
    Q.put((0, s))
    dist[s] = 0

    while not Q.empty():
        d, u = Q.get()
        if d > dist[u]:
            continue

        for v, g in G[u]:
            if relax(G, u, v, g, dist):
                Q.put((dist[v], v))

    if dist[t] == inf:
        return None
    else:
        return dist[t]
def spacetravel( n, E, S, a, b ):
    G = [[] for _ in range(n)]
    for edge in E:
        u, v, g = edge
        G[u].append((v, g))
        G[v].append((u, g))

    for s1 in S:
        for s2 in S:
            if s1 != s2:
                G[s1].append((s2, 0))

    return dijkstra(G, a, b)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
