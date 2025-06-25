from math import inf


def dfs_visit(G, u, v, visited, opts):
    n = len(G)
    visited[u][v] = True

    for x in range(n):
        for y in range(n):
            if x == y or (x, y) == (v, u):
                continue
            if not visited[x][y] and opts[x][y] and (u == x or G[u][x] < inf) and (v == y or G[v][y] < inf):
                dfs_visit(G, x, y, visited, opts)


def dfs(G, opts, s, t):
    n = len(G)
    visited = [[False]*n for _ in range(n)]
    dfs_visit(G, s, t, visited, opts)
    return visited[t][s]

def warshall(G):
    n = len(G)
    dist = [row[:] for row in G]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def is_safe(G, d, s, t):
    n = len(G)
    dist = warshall(G)
    opts = [[True if dist[x][y] >= d else False for x in range(n)] for y in range(n)]
    return dfs(G, opts, s, t)


# d = 4
# G = [[0, 3, 4, inf, inf], [3, 0, 8, 3, inf], [4, 8, 0, 5, inf], [inf, 3, 5, 0, 1], [inf, inf, inf, 1, 0]]
# G = [[0, 3, 3, inf, inf], [3, 0, 8, 3, inf], [3, 8, 0, 3, inf], [inf, 3, 3, 0, 1], [inf, inf, inf, 1, 0]]
# G = [[0, 3, 3, inf, inf], [3, 0, 2, 3, inf], [3, 2, 0, 3, inf], [inf, 3, 3, 0, 1], [inf, inf, inf, 1, 0]]
#
#
# print(is_safe(G, d, 0, 4))
