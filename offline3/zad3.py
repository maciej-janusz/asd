from zad3testy import runtests
from collections import deque
from math import inf


def bfs(G, s):
    n = len(G)
    dist = [inf] * n
    count = [0] * n
    q = deque([s])
    dist[s] = 0
    count[s] = 1

    while q:
        u = q.popleft()
        for v in G[u]:
            if dist[v] == inf:
                dist[v] = dist[u] + 1
                count[v] = count[u]
                q.append(v)
            elif dist[u] + 1 == dist[v]:
                count[v] += count[u]

    return dist, count

def longer( G, s, t ):
    n = len(G)

    dist_s, count_s = bfs(G, s)
    dist_t, count_t = bfs(G, t)

    shortest = dist_s[t]
    cnt = count_s[t]
    for v in range(n):
        for u in G[v]:
            if v > u:
                continue
            if dist_s[v] + 1 + dist_t[u] == shortest:
                if count_s[v]*count_t[u] == cnt:
                    return (u, v)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
