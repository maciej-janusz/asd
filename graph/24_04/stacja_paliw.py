from math import inf
from queue import PriorityQueue

def get_path(s, t, fuel, parent):
    path = [(t, fuel)]
    while t != s:
        t, fuel = parent[t][fuel]
        path.append((t, fuel))
    return path[::-1]


def dijkstra_cheapest_cost(G, D, prices, s, t):
    n = len(G)
    min_cost = [[inf]*(D+1) for _ in range(n)]
    parent = [[None]*(D+1) for _ in range(n)]

    Q = PriorityQueue()
    Q.put((0, s, 0))

    min_cost[s][0] = 0

    while not Q.empty():
        cost, u, fuel = Q.get()
        if cost > min_cost[u][fuel]:
            continue

        for v, dist in G[u]:
            for i in range(D-fuel+1):
                if fuel + i >= dist and min_cost[v][fuel + i - dist] > min_cost[u][fuel] + prices[u] * i:
                    min_cost[v][fuel + i - dist] = min_cost[u][fuel] + prices[u] * i
                    parent[v][fuel + i - dist] = (u, fuel)
                    Q.put((min_cost[v][fuel + i - dist], v, fuel+i-dist))

    path = get_path(s, t, 0, parent)
    for i in range(len(path)-1):
        u, fuel_u = path[i]
        v, fuel_v = path[i+1]

        dist = inf
        for t, d in G[u]:
            if t == v:
                dist = d

        to_tank = fuel_v - fuel_u + dist
        path[i] = (u, to_tank)

    return min_cost[t][0], path


G = [
    [(1, 40), (2, 45)],
    [(0, 40), (3, 35), (4, 20)],
    [(0, 45), (3, 30)],
    [(1, 35), (2, 30), (5, 10)],
    [(1, 20), (6, 15)],
    [(3, 10), (6, 40)],
    [(4, 15), (5, 60)],
]
prices = [5, 4, 1, 10, 8, 6, 10]

print(dijkstra_cheapest_cost(G, 50, prices, 0, 6))
