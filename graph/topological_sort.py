def topological_sort(G):
    n = len(G)
    top_sort = []
    visited = [False]*n

    def visit(G, v):
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                visit(G, u)
        top_sort.append(v)

    for v in range(n):
        if not visited[v]:
            visit(G, v)

    return top_sort[::-1]

