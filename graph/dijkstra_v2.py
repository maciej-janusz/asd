from math import inf

def relax(G, u, v, parent, dist):
    if G[u][v] > 0 and dist[u] + G[u][v] < dist[v]:
        dist[v] = dist[u] + G[u][v]
        parent[v] = u

def dijkstra(G, s):
    n = len(G)
    dist = [inf]*n
    visited = [False]*n
    parent = [None]*n

    dist[s] = 0
    while True:
        mini = inf
        u = -1
        for v in range(n):
            if not visited[v] and dist[v] < mini:
                u = v
                mini = dist[v]
        if u == -1:
            break

        visited[u] = True
        for v in range(n):
            relax(G, u, v, parent, dist)

    return dist, parent