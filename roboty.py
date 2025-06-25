R = [(1, 4), (2, 2), (3, 3), (4, 1)]
E = [False, False, False, False]

R = [(1, 1), (2, 2)]
E = [False, False]

def fight(R, E):
    n = len(R)
    if sum(E) == n:
        return True

    ret = False
    for i in range(n):
        if E[i]: continue
        ai, bi = R[i]
        for j in range(n):
            if E[j]: continue
            aj, bj = R[j]
            if ai > aj or bi > bj:
                E[j] = True
            if aj > ai or bj > bi:
                E[i] = True
            if not E[i] and not E[j]:
                continue
            ret = ret or fight(R, E)
            E[i] = False
            E[j] = False

    return ret

print(fight(R, E))

