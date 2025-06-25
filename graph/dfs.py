#O(V+E)
def dfs(G):
    n = len(G)
    time = 0
    visited = [False]*n
    parent = [None]*n

    def visit(G, v):
        nonlocal time
        visited[v] = True
        time += 1
        for u in G[v]:
            if not visited[u]:
                parent[u] = v
                visit(G, u)
        time += 1

    for v in range(n):
        if not visited[v]:
            visit(G, v)

    return parent, visited