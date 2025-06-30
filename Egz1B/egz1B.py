#Maciej Janusz
"""
    Sortujemy pracwonikow topologiczne, aby upewnic sie ze przejdziemy po nich w dobrej kolejnosci.
    Startujac z kazdego pracownika liczymy na ile sposobow mozemy dojsc do kolejnych pracwonikow.
    Jeżeli do danego pracwonika u da sie dojsc na jeden sposob to krawedz (parent[u], u) jest delegacja krytyczna.
    Zapamietujemy ktore krawedzie sa delegacjami krytycznymi i zliczamy je na koniec.
    O(V(E+V))
"""
from egz1Btesty import runtests


def topo_sort(G):
    n = len(G)
    visited = [0] * n
    order = []

    def visit(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                visit(v)
        order.append(u)

    for u in range(n):
        if not visited[u]:
            visit(u)

    return order[::-1]


def find(G, idx, order, C):
    n = len(G)
    cnt = [0]*n
    parent = [None]*n
    s = order[idx]

    cnt[s] = 1
    for i in range(idx, n):
        u = order[i]
        if cnt[u] == 0:
            continue
        if cnt[u] == 1 and parent[u] is not None:
            C[parent[u]][u] = True

        for v in G[u]:
            cnt[v] += cnt[u]
            parent[v] = u


def critical(V, E):
    G = [[] for _ in range(V)]
    for u, v in E:
        G[u].append(v)

    order = topo_sort(G)
    C = [[False]*V for _ in range(V)]
    for idx in range(V):
        find(G, idx, order, C)

    res = 0
    for i in range(V):
        for j in range(V):
            if C[i][j]:
                res += 1
                
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests = True)
