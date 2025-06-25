from math import inf
from kol2atesty import runtests

def drivers_rek( P, B ):
    LIMIT = 3
    n = len(P)
    P = [(P[i][0], P[i][1], i) for i in range(n)]
    P.sort()

    memo = {}
    def f(driver, i, j):
        if (driver, i, j) in memo:
            return memo[(driver, i, j)]

        if i == B or i > n-1:
            return 0, []

        best = inf
        best_changes = []
        if P[i][1]:
            val, changes = f(not driver, i + 1, 1)
            if val < best:
                best = val
                best_changes = [P[i][2]] + changes
            if j < LIMIT:
                val, changes = f(driver, i + 1, j + 1)
                if val < best:
                    best = val
                    best_changes = changes
        else:
            if driver:
                val, changes = f(driver, i + 1, j)
                val += 1
                if val < best:
                    best = val
                    best_changes = changes
            else:
                val, changes = f(driver, i + 1, j)
                if val < best:
                    best = val
                    best_changes = changes

        memo[(driver, i ,j)] = best, best_changes
        return best, best_changes


    val, changes = f(False, 0, 1)

    return changes

def drivers( P, B ):
    LIMIT = 3
    P = [(P[i][0], P[i][1], i) for i in range(len(P)) if P[i][0] < B]
    P.append((B, False, len(P)))
    n = len(P)

    P.sort()

    cost = [[[inf for _ in range(2)] for _ in range(LIMIT)] for _ in range(n)]
    changes = [[[[] for _ in range(2)] for _ in range(LIMIT)] for _ in range(n)]

    for j in range(LIMIT):
        for driver in range(2):
            cost[n-1][j][driver] = 0

    for i in range(n-2, -1, -1):
        for j in range(LIMIT):
            for driver in range(2):
                if P[i][1]:
                    val = cost[i + 1][0][1-driver]
                    if val < cost[i][j][driver]:
                        cost[i][j][driver] = val
                        changes[i][j][driver] = [P[i][2]] + changes[i + 1][0][1-driver]
                    if j < LIMIT-1:
                        val = cost[i + 1][j + 1][driver]
                        if val < cost[i][j][driver]:
                            cost[i][j][driver] = val
                            changes[i][j][driver] = changes[i + 1][j + 1][driver]
                else:
                    if driver:
                        val = cost[i + 1][j][driver]+1
                        if val < cost[i][j][driver]:
                            cost[i][j][driver] = val
                            changes[i][j][driver] = changes[i + 1][j][driver]
                    else:
                        val = cost[i + 1][j][driver]
                        if val < cost[i][j][driver]:
                            cost[i][j][driver] = val
                            changes[i][j][driver] = changes[i + 1][j][driver]


    return changes[0][0][0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )