#O(V+E)
def dfs(G):
    n = len(G)
    time = 0
    visited = [False]*n
    parent = [None]*n

    def visit(u):
        nonlocal time
        visited[u] = True
        time += 1
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                visit(v)
        time += 1

    for u in range(n):
        if not visited[u]:
            visit(u)

    return parent, visited