def strongly_connected_components(G):
    def visit(G, v, visited, order=None, component=None):
        visited[v] = True
        if component is not None:
            component.append(v)
        for u in G[v]:
            if not visited[u]:
                visit(G, u, visited, order, component)
        if order is not None:
            order.append(v)

    n = len(G)
    visited = [False] * n
    order = []
    for v in range(n):
        if not visited[v]:
            visit(G, v, visited, order=order)

    G2 = [[] for _ in range(n)]
    for i, items in enumerate(G):
        for item in items:
            G2[item].append(i)

    visited = [False] * n
    res = []
    for v in reversed(order):
        if not visited[v]:
            component = []
            visit(G2, v, visited, component=component)
            res.append(component)

    return res
