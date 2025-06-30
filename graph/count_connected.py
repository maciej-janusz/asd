def count_connected(G):
    n = len(G)
    counter = 0
    visited = [False] * n

    def visit(u):
        n = len(G)
        visited[u] = True
        for v in range(n):
            if G[u][v] and not visited[v]:
                visit(v)

    for u in range(n):
        if not visited[u]:
            counter += 1
            visit(u)
    return counter

