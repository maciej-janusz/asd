from kol2btesty import runtests
from math import inf
import heapq


def min_cost_n2( O, C, T, L ):
    arr = [(0, 0)] + [(O[i], C[i]) for i in range(len(O)) if O[i] < L] + [(L, 0)]
    arr.sort()
    n = len(arr)
    max_range = T

    dp = [[inf]*2 for _ in range(n)]
    dp[0][0] = 0
    dp[0][1] = 0

    for i in range(1, n):
        for j in range(i-1, -1, -1):
            d = arr[i][0] - arr[j][0]
            if d <= max_range:
                dp[i][0] = min(dp[i][0], dp[j][0] + arr[i][1])
                dp[i][1] = min(dp[i][1], dp[j][1] + arr[i][1])
            if d <= 2*max_range:
                dp[i][1] = min(dp[i][1], dp[j][0] + arr[i][1])
            else:
                break

def min_cost(O, C, T, L):
    arr = [(0, 0)] + [(O[i], C[i]) for i in range(len(O)) if O[i] < L] + [(L, 0)]
    arr.sort()
    n = len(arr)

    dist = [[inf] * 2 for _ in range(n)]
    dist[0][0] = 0

    pq = [(0, 0, 0)]

    while pq:
        cost_u, u, used = heapq.heappop(pq)
        if cost_u > dist[u][used]:
            continue

        for v in range(u + 1, n):
            d = arr[v][0] - arr[u][0]
            if d > 2 * T:
                break

            new_cost = cost_u + arr[v][1]
            if d <= T and dist[v][used] > new_cost:
                dist[v][used] = new_cost
                heapq.heappush(pq, (new_cost, v, used))

            if d <= 2 * T and used == 0 and dist[v][1] > new_cost:
                dist[v][1] = new_cost
                heapq.heappush(pq, (new_cost, v, 1))

    return dist[-1][1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )