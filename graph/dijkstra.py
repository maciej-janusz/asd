#O((V+E)logV)
from queue import PriorityQueue
from math import inf

def relax(u, v, g, dist, parent):
    if dist[u]+g<dist[v]:
        dist[v] = dist[u]+g
        parent[v] = u
        return True
    return False

def dijkstra(G, s):
    n = len(G)
    dist = [inf] * n
    parent = [None] * n

    Q = PriorityQueue()
    Q.put((0, s))
    dist[s] = 0

    while not Q.empty():
        d, u = Q.get()
        if d > dist[u]:
            continue

        for v, g in G[u]:
            if relax(u, v, g, dist, parent):
                Q.put((dist[v], v))

    return dist, parent

