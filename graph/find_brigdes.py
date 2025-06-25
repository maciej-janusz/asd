from math import inf

def find_bridges(G):
    n = len(G)
    d = [inf] * n
    low = [inf] * n
    parent = [None] * n
    bridges = []
    time = 0

    def visit(u):
        nonlocal time
        d[u] = low[u] = time
        time += 1

        for v in G[u]:
            if d[v] == inf:
                parent[v] = u
                visit(v)
                low[u] = min(low[u], low[v])
                if d[u] < low[v]:
                    bridges.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], d[v])

    for u in range(n):
        if d[u] == inf:
            visit(u)

    return bridges