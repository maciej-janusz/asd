from math import inf
from queue import PriorityQueue

def relax(u, v, g, max_min_weight, parent, visited):
    if not visited[v] or max_min_weight[v] < min(max_min_weight[u], g):
        max_min_weight[v] = min(max_min_weight[u], g)
        visited[v] = True
        parent[v] = u
        return True
    return False

def dijkstra_max_min_weight(G, s, t):
    n = len(G)
    max_min_weight = [inf] * n
    visited = [False] * n
    parent = [None] * n

    Q = PriorityQueue()
    visited[s] = True
    Q.put((-inf, s))

    while not Q.empty():
        d, u = Q.get()
        d = -d
        if d < max_min_weight[u]:
            continue

        for v, g in G[u]:
            if relax(u, v, g, max_min_weight, parent, visited):
                Q.put((-max_min_weight[v], v))

    return max_min_weight[t], parent


graph = [
    [(1, 2), (2, 3)],    # 0 → 1 (2), 2 (3)
    [(0, 2), (3, 4)],    # 1 → 0 (2), 3 (4)
    [(0, 3), (3, 1)],    # 2 → 0 (3), 3 (1)
    [(1, 4), (2, 1)]     # 3 → 1 (4), 2 (1)
]

s, t = 0, 3  # Start from node 0, find the max-min weight to node 3
max_min_weight, parent = dijkstra_max_min_weight(graph, s, t)

print(f"Max-min weight from {s} to {t}: {max_min_weight}")
