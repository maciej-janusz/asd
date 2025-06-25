from math import inf


def get_path(s, t, parent):
    path = [t]
    prev = -1
    while s != t:
        t, prev = [x for x in parent[t] if x[1] > prev][0]
        path.append(t)
    return path[::-1]


def shortest_desc_order(G, s, t):
    n = len(G)
    edges = []

    for u in range(n):
        for v, g in G[u]:
            edges.append((u, v, g))
    edges.sort(key=lambda x: -x[2])

    parent = [[] for _ in range(n)]
    last = [inf]*n
    dist = [inf] * n
    dist[s] = 0
    for u, v, g in edges:
        if dist[v] > dist[u] + g and g < last[u]:
            dist[v] = dist[u] + g
            last[v] = g
            parent[v].append((u, g))

    return dist[t], get_path(s, t, parent)

G = [
    [
        (1, 10), (2, 4)
    ],
    [
        (0, 10), (3, 5)
    ],
    [
        (0, 4), (3, 1), (4, 6)
    ],
    [
        (1, 5), (2, 1), (4, 3)
    ],
    [
        (3, 3), (2, 6)
    ]
]
print(shortest_desc_order(G, 0, 4))

G = [[(1, 2), (3, 4)], [(0, 2), (2, 3)], [(1, 3), (4, 4)], [(0, 4), (4, 5)], [(3, 5), (2, 4), (5, 5)], [(4, 5)]]
print(shortest_desc_order(G, 5, 0))