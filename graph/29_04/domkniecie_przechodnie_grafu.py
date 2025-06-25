def warshall(G):
    n = len(G)
    dist = [row[:] for row in G]
    gprim = [[False]*n for _ in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    gprim[i][j] = True

    return gprim
