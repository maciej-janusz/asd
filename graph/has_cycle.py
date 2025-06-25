def has_cycle(G):
    n = len(G)
    visited = [0] * n

    def visit(v):
        visited[v] = 1
        for u in G[v]:
            if visited[u] == 1:
                return True
            if visited[u] == 0 and visit(u):
                return True
        visited[v] = 2
        return False

    for v in range(n):
        if visited[v] == 0:
            if visit(v):
                return True
    return False
