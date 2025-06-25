def count_connected(G):
    n = len(G)
    counter = 0
    visited = [False] * n

    def visit(G, s):
        n = len(G)
        visited[s] = True
        for i in range(n):
            if G[s][i] and not visited[i]:
                visit(G, i)

    for i in range(n):
        if not visited[i]:
            counter += 1
            visit(G, i)
    return counter

