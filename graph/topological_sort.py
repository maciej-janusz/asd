def topological_sort(G):
    n = len(G)
    top_sort = []
    visited = [False]*n

    def visit(G, u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                visit(G, v)
        top_sort.append(u)

    for u in range(n):
        if not visited[u]:
            visit(G, u)

    return top_sort[::-1]

