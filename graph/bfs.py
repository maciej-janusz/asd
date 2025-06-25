#O(V+E)
from collections import deque
from math import inf

def bfs(G, s):
    n = len(G)
    Q = deque()
    visited = [False]*n
    parent = [None]*n
    d = [inf]*n

    d[s] = 0
    visited[s] = True
    Q.append(s)

    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
                Q.append(v)

    return parent, visited, d