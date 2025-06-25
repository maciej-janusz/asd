#O(V*W+E)
from collections import deque
from math import inf

def bfs(G, s, t, max_w):
    n = len(G)
    dist = [[inf]*(max_w+1) for _ in range(n)]
    Q = deque()

    dist[s][0] = 0
    Q.append((s, 0))

    while Q:
        u, d = Q.popleft()
        if d > 0:
            if dist[u][d - 1] > dist[u][d] + 1:
                dist[u][d - 1] = dist[u][d] + 1
                Q.append((u, d - 1))
        else:
            for v, g in G[u]:
                if dist[v][g-1] > dist[u][d] + 1:
                    dist[v][g-1] = dist[u][d] + 1
                    Q.append((v, g-1))

    return dist[t][0]

G = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}
print(bfs(G, 0, 3, 5))
