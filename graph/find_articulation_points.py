from math import inf

def find_articulation_points(G):
    n = len(G)
    d = [inf] * n
    low = [inf] * n
    parent = [None] * n
    articulation_points = set()
    time = 0

    def visit(u):
        nonlocal time
        d[u] = low[u] = time
        time += 1
        children = 0

        for v in G[u]:
            if d[v] == inf:
                parent[v] = u
                children += 1
                visit(v)
                low[u] = min(low[u], low[v])

                if parent[u] is not None and d[u] <= low[v]:
                    articulation_points.add(u)

            elif v != parent[u]:
                low[u] = min(low[u], d[v])

        if parent[u] is None and children > 1:
            articulation_points.add(u)

    for u in range(n):
        if d[u] == inf:
            visit(u)

    return articulation_points
