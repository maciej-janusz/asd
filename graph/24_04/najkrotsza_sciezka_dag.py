from math import inf

def dfs_visit(G, u, visited, res):
    visited[u] = True
    for v, _ in G[u]:
        if not visited[v]:
            dfs_visit(G, v, visited, res)
    res.append(u)

def topo_sort(G):
    n = len(G)
    res = []
    visited = [False] * n

    for u in range(n):
        if not visited[u]:
            dfs_visit(G, u, visited, res)

    return res[::-1]

def relax(u, v, g, dist):
    if dist[u] + g < dist[v]:
        dist[v] = dist[u] + g
        return True
    return False

def get_path(parent, s, t):
    res = [t]
    u = parent[t]
    while u is not None:
        res.append(u)
        if u == s:
            break
        u = parent[u]
    return res[::-1]

def shortest_DAG(G, s, t):
    topo = topo_sort(G)
    n = len(G)
    dist = [inf]*n
    parent = [None]*n
    dist[s] = 0

    for u in topo:
        for v, g in G[u]:
            if dist[u] + g < dist[v]:
                dist[v] = dist[u] + g
                parent[v] = u

    return dist[t], get_path(parent, s, t)

graph = [
    [(1, 2), (2, 3)],  # 0 → 1 (2), 2 (3)
    [(3, 4)],          # 1 → 3 (4)
    [(3, 1), (4, 6)],  # 2 → 3 (1), 4 (6)
    [(4, 2)],          # 3 → 4 (2)
    []                 # 4 → no outgoing edges
]

print(shortest_DAG(graph, 0, 3))