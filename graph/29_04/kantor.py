from math import log10, inf

def ford(G):
    n = len(G)
    dist = [inf]*n
    dist[0] = 0
    edges = []
    for u in range(n):
        for v in range(n):
            if G[u][v] > 0:
                g = -log10(G[u][v])
                edges.append((u, v, g))



    for _ in range(n-1):
        for u, v, g in edges:
            if dist[v] > dist[u] + g:
                dist[v] = dist[u] + g

    for u, v, g in edges:
        if dist[v] > dist[u] + g:
            return True

    return False







G = [
    # PLN     USD     EUR     GBP
    [ 0.00,   0.23,   0.21,   0.00 ],  # PLN
    [ 4.25,   0.00,   0.91,   0.00 ],  # USD
    [ 4.75,   1.10,   0.00,   0.87 ],  # EUR
    [ 0.00,   0.00,   1.15,   0.00 ]   # GBP
]
print(ford(G))

G = [
    # PLN     USD     EUR     GBP
    [ 0.00,   0.23,   0.21,   0.00 ],  # PLN
    [ 4.25,   0.00,   0.91,   0.00 ],  # USD
    [ 5.00,   1.10,   0.00,   0.87 ],  # EUR
    [ 0.00,   0.00,   1.15,   0.00 ]   # GBP
]
print(ford(G))

G = [
    # PLN     USD     EUR     GBP
    [ 1.00,   0.25,   0.25 * 0.9,  0.25 * 0.9 * 0.8 ],  # PLN
    [ 1/0.25, 1.00,   0.9,        0.9 * 0.8 ],          # USD
    [ 1/(0.25*0.9), 1/0.9, 1.00,  0.8 ],                # EUR
    [ 1/(0.25*0.9*0.8), 1/(0.9*0.8), 1/0.8, 1.00 ]       # GBP
]
print(ford(G))

G = [
    #PLN   #USD  #EUR  #GBP
    [1.00, 0.25, 0.20, 0.16],   # PLN
    [4.00, 1.00, 0.80, 0.50],   # USD
    [5.00, 1.25, 1.00, 0.80],   # EUR
    [6.25, 2.00, 1.25, 1.00]    # GBP
]
print(ford(G))