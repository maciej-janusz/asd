from math import inf
from queue import PriorityQueue


def dijksta_min_B(G, s, t):
    n = len(G)
    distA = [inf] * n
    distB = [inf] * n
    parentA = [None] * n
    parentB = [None] * n

    Q = PriorityQueue()
    distA[s] = 0
    distB[s] = 0
    Q.put((0, s, False))
    Q.put((0, s, True))

    while not Q.empty():
        d, u, after_a = Q.get()
        if after_a:
            if d > distA[u]:
                continue
            for v, _ in G[u]:
                if distB[v] > distA[u]:
                    distB[v] = distA[u]
                    parentB[v] = u
                    Q.put((distB[v], v, False))
        else:
            if d > distB[u]:
                continue
            for v, g in G[u]:
                if distA[v] > distB[u]+g:
                    distA[v] = distB[u]+g
                    parentA[v] = u
                    Q.put((distA[v], v, True))

    u = t
    path = [u]
    after_a = distA[u] < distB[u]
    first = ""
    while u != s:
        if after_a:
            path.append(parentA[u])
            u = parentA[u]
            after_a = False
            first = "B"
        else:
            path.append(parentB[u])
            u = parentB[u]
            after_a = True
            first = "A"

    return min(distA[t], distB[t]), path[::-1], first

G = [
    [
        (1, 3), (2, 4) #0
    ],
    [
        (0, 3), (3, 5) #1
    ],
    [
        (0, 4), (3, 1), (4, 6) #2
    ],
    [
        (1, 5), (2, 1), (4, 10) #3
    ],
    [
        #4
    ]
]
print(dijksta_min_B(G, 0, 4))