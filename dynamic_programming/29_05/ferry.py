"""
prom o dlugosci l i 2 pasach
upakowac jak najwiecej aut o roznych dlugosciach (wjezdzaja po koleje, tylko wybieramy pas)
"""
"""
1. f(l, r, x) = l - metrow lewego, r - metrow prawego, k - pojazdow, -> czy mozna upchac
2. f(l, r, x) = f(i-A[x], j, x-1) or f(i, j-A[x], x-1)
3. 
"""

def ferry_rec(L, N, A):
    memo = {}

    def rec(l, r, k):
        if (l, r, k) in memo:
            return memo[(l, r, k)]

        if l < 0 or r < 0:
            result = False
        elif k == 0:
            result = True
        else:
            result = rec(l-A[k-1], r, k-1) or rec(l, r-A[k-1], k-1)

        memo[(l, r, k)] = result
        return result

    for k in range(N, -1, -1):
        if rec(L, L, k):
            return k

L = 10
N = 5
A = [3, 4, 2, 5, 7]

print(ferry_rec(L, N, A))

