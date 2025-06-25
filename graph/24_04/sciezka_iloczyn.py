from math import inf, log10
from queue import PriorityQueue

def relax(u, v, g, dist):
    if dist[u] + g < dist[v]:
        dist[v] = dist[u] + g
        return True
    return False

def dijkstra_multiply(G, s, t):
    n = len(G)
    G2 = [[(v, log10(g)) for v, g in G[u]] for u in range(n)]
    dist = [inf] * n

    Q = PriorityQueue()
    dist[s] = 0
    Q.put((0, s))

    while not Q.empty():
        d, u = Q.get()
        if d > dist[u]:
            continue

        for v, g in G2[u]:
            if relax(u, v, g, dist):
                Q.put((dist[v], v))

    return 10**dist[t]

graph = [
    [(1, 2), (2, 3)],
    [(2, 2)],
    []
]

print(dijkstra_multiply(graph, 0, 2))