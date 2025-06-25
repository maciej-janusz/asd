def unique_sum_rec(A, T):
    memory = {}
    n = len(A)

    def rec(t, i):
        if (t, i) in memory:
            return memory[(t, i)]

        if t == 0:
            result = True
        elif t < 0 or (t > 0 and i < 0):
            result = False
        else:
            result = rec(t-A[i], i-1) or rec(t, i-1)

        memory[t] = result
        return result

    return rec(T, n-1)


def unique_sum(A, T):
    n = len(A)
    F = [[False] * (T + 1) for _ in range(n)]

    for i in range(n):
        F[i][0] = True

    if A[0] <= T:
        F[0][A[0]] = True

    for i in range(1, n):
        for t in range(1, T + 1):
            F[i][t] = F[i - 1][t] or (t >= A[i] and F[i - 1][t - A[i]])

    return F[n - 1][T]


A = [8, 7, 9, 1, 16, 31, 5]
T = 24

print(unique_sum_rec(A, T), unique_sum(A, T))