from math import inf

def coins_problem_rec(T, M):
    memory = {}

    def rec(t):
        if t in memory:
            return memory[t]
        if t == 0:
            result = 0
        elif t < 0:
            result = inf
        else:
            result = inf
            for m in M:
                result = min(rec(t-m)+1, result)
            memory[t] = result
        return result

    return rec(T)

def coins_problem(T, M):
    n = T+1
    F = [inf]*n
    F[0] = 0

    for c in range(1, n):
        for m in M:
            if c - m >= 0:
                F[c] = min(F[c], F[c-m]+1)

    return F[T]


T = 12
M = [2, 4, 5]

print(coins_problem(T, M), coins_problem_rec(T, M))
