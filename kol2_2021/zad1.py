from zad1testy import runtests
from math import inf
from collections import deque

def get_path(parent, t, s):
    x, y = t, s
    path = [(x, y)]
    while x != s or y != t:
        x, y = parent[x][y]
        path.append((x, y))
    return path[::-1]


def warshall(G):
    n = len(G)
    dist = [[inf if G[x][y] == 0 and x != y else G[x][y] for y in range(n)] for x in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def bfs(G, opts, s, t):
    n = len(G)
    visited = [[False]*n for _ in range(n)]
    parent = [[(None, None)]*n for _ in range(n)]
    q = deque()

    q.append((s, t))
    visited[s][t] = True
    while q:
        u, v = q.popleft()
        for x in range(n):
            for y in range(n):
                if x == y or (x, y) == (v, u):
                    continue
                if not visited[x][y] and opts[x][y] and (x == u or G[u][x] > 0) and (y == v or G[v][y] > 0):
                    parent[x][y] = (u, v)
                    visited[x][y] = True
                    q.append((x, y))

    return get_path(parent, t, s)

def keep_distance(M, x, y, d):
    n = len(M)
    dist = warshall(M)
    opts = [[dist[i][j] >= d for j in range(n)] for i in range(n)]
    return bfs(M, opts, x, y)


runtests( keep_distance )