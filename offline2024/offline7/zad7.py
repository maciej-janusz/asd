from zad7testy import runtests
from math import inf

def maze( L ):
    n = len(L)
    memo = {}

    def f(x, y, dy):
        if (x, y, dy) in memo:
            return memo[(x, y, dy)]
        if x == n-1 and y == n-1:
            return 0
        if min(x, y) < 0 or max(x, y) >= n or L[y][x] == '#':
            return -inf

        best = -inf
        if dy != 1:
            best = max(best, f(x, y-1, -1)+1)
        if dy != -1:
            best = max(best, f(x, y+1, 1)+1)
        best = max(best, f(x+1, y, 0)+1)

        memo[(x, y, dy)] = best
        return best


    return max(f(0, 0, 0), -1)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )