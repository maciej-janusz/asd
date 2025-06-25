from collections import deque

def bipartite(G):
    n = len(G)
    color = [-1]*n

    Q = deque()
    Q.append(0)
    color[0] = 0
    while Q:
        v = Q.popleft()
        for u in G[v]:
            if color[u] == color[v]:
                return False
            elif color[u] == -1:
                color[u] = 1 - color[v]
                Q.append(u)
    return True


G = [[6, 7, 6], [5, 7], [6, 7], [8, 8, 7], [6], [1], [0, 2, 4, 0], [1, 2, 3, 0], [3, 3]]

print(bipartite(G))