from math import inf

def cities_list(cities):
    res = []
    i = 0
    while cities > 0:
        curr = cities%2
        if curr:
            res.append(i)
        cities //= 2
        i += 1
    return res


def rec_tsp(cities, t, dist, F):
    if F[cities][t] < inf:
        return F[cities][t]

    for r in cities_list(cities):
        if r == t: continue
        F[cities][t] = min(F[cities][t], rec_tsp(cities & ~(1 << t), r, dist, F) + dist[r][t])


    return F[cities][t]

def tsp(dist, source, n):
    F = [[inf]*n for _ in range(pow(2, n))]
    F[1<<source][source] = 0

    best = inf
    all_cities = (1 << n) - 1
    for t in range(n):
        if t == source:
            continue
        best = min(best, rec_tsp(all_cities, t, dist, F) + dist[t][source])
    return best

dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print("Minimum TSP cost:", tsp(dist_matrix, 0, 4))