from kol1testy import runtests


def quick_select(T, l, p, idx):
    if l == p:
        return T[l]
    mid = (l+p)//2
    T[mid], T[p] = T[p], T[mid]
    x = T[p]
    i = l - 1
    for j in range(l, p):
        if T[j] < x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[p] = T[p], T[i+1]

    if i + 1 == idx:
        return T[i+1]
    elif i + 1 > idx:
        return quick_select(T, l, i, idx)
    else:
        return quick_select(T, i+2, p, idx)
def ksum(T, k, p):
    res = 0
    n = len(T)
    for i in range(n-p+1):
        idx = p-k
        res += quick_select(T[i:i+p], 0, p-1, idx)

    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
