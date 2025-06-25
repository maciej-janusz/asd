from math import sqrt, inf


def dist(i, j):
    return sqrt((i[0] - j[0]) * (i[0] - j[0]) + (i[1] - j[1]) * (i[1] - j[1]))

def tsp2d(M):
    n = len(M)
    if n < 2:
        return 0  # Handle cases with 0 or 1 points

    D = [[dist(M[i], M[j]) for j in range(n)] for i in range(n)]
    dp = [[inf] * n for _ in range(n)]
    dp[0][1] = D[0][1]  # Distance from 0 to 1

    def rec(i, j):
        if dp[i][j] != inf:
            return dp[i][j]

        if i == j - 1:
            # Path ending at j, need to find best k to j-1
            best = inf
            for k in range(j - 1):
                current = rec(k, j - 1) + D[k][j]
                if current < best:
                    best = current
            dp[i][j] = best
        else:
            # Extend the path from i to j-1
            dp[i][j] = rec(i, j - 1) + D[j - 1][j]
        return dp[i][j]

    # Find the minimum tour by connecting back to 0
    best = inf
    for k in range(n - 1):
        current = rec(k, n - 1) + D[k][n-1]
        if current < best:
            best = current

    return best

points = [
    (0, 0), (2, 3), (5, 4), (1, 1),
    (6, 1), (3, 0), (4, 2), (0, 4)
]
print(tsp2d(points))