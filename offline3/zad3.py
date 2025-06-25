from zad3testy import runtests
from collections import deque
from math import inf, isinf

def longer( G, s, t ):
    n = len(G)

    dist_s = [inf] * n
    count_s = [0] * n
    q = deque([s])
    dist_s[s] = 0
    count_s[s] = 1

    while q:
        v = q.popleft()
        for u in G[v]:
            if isinf(dist_s[u]):
                dist_s[u] = dist_s[v]+1
                count_s[u] = count_s[v]
                q.append(u)
            elif dist_s[v] + 1 == dist_s[u]:
                count_s[u] += count_s[v]
    if isinf(dist_s[t]):
        return None

    dist_t = [inf] * n
    count_t = [0] * n
    q = deque([t])
    dist_t[t] = 0
    count_t[t] = 1

    while q:
        v = q.popleft()
        for u in G[v]:
            if isinf(dist_t[u]):
                dist_t[u] = dist_t[v] + 1
                count_t[u] = count_t[v]
                q.append(u)
            elif dist_t[v] + 1 == dist_t[u]:
                count_t[u] += count_t[v]

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
