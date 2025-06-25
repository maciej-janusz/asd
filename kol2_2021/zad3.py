from zad3testy import runtests
from zad3EK import edmonds_karp
from math import inf


def warshall(graph):
    n = len(graph)
    dist = [[inf if graph[x][y] == 0 and x != y else graph[x][y] for y in range(n)] for x in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
def BlueAndGreen(T, K, D):
    n = len(T)
    dist = warshall(T)

    size = len(T)+2
    source = n
    sink = n + 1
    graph = [[0] * size for _ in range(size)]
    for i in range(n):
        for j in range(n):
            if dist[i][j] >= D:
                graph[i][j] = 1

    for i in range(n):
        if K[i] == 'B':
            graph[i][source] = graph[source][i] = 1
        elif K[i] == 'G':
            graph[i][sink] = graph[sink][i] = 1

    return edmonds_karp(graph, sink, source)

runtests( BlueAndGreen ) 
