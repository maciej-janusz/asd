from zad3testy import runtests
from collections import deque
from math import inf

def bfs(G, s, t, deleted=(-1,-1)):
    Q = deque()
    n = len(G)
    visited = [False]*n
    d = [inf]*n
    visited[s] = True
    d[s] = 0
    Q.append(s)
    while Q:
        v = Q.popleft()
        for u in G[v]:
            if deleted == (v, u) or deleted == (u, v):
                continue
            if not visited[u]:
                if u == t:
                    return d[v] + 1
                d[u] = d[v] + 1
                visited[u] = True
                Q.append(u)
    return inf
def longer( G, s, t ):
    d = bfs(G, s, t)
    if d == inf: return None

    for i in range(len(G)):
        for j in range(len(G[i])):
            new_d = bfs(G, s, t, (i, G[i][j]))
            if new_d > d:
                return (i, G[i][j])
    print(G)
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
