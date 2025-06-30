def dfs(G):
    def visit(G, u, res):
        n = len(G)
        for v in range(n):
            if G[u][v] == 0 or G[u][v] == 0:
                continue
            G[u][v] = G[v][u] = 0
            visit(G, v)
        res.append(u)

    res = []
    visit(G, 0, res)

    return res[::-1]


def euler_cycle(G):
    if len(G) < 2:
        return None
    for i in range(len(G)):
        if sum(G[i]) % 2 == 1:
            return None

    return dfs(G)