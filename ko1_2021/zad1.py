from zad1testy import runtests


def hoare(T, l, r):
    pivot = T[l]
    l -= 1
    r += 1

    while True:
        l += 1
        while T[l] < pivot:
            l += 1

        r -= 1
        while T[r] > pivot:
            r -= 1

        if l >= r:
            return r
        T[l], T[r] = T[r], T[l]

def quick_sort(T, l, r):
    if l < r:
        q = hoare(T, l, r)
        quick_sort(T, l, q)
        quick_sort(T, q+1, r)



def Median(T):
    n = len(T)
    merged = []
    for x in T:
        merged.extend(x)
    quick_sort(merged, 0, n*n-1)

    l = 0
    m = int(n*(n-1)/2)
    r = int(n*(n+1)/2)
    for i in range(n):
        for j in range(n):
            if i == j:
                T[i][j] = merged[m]
                m += 1
            elif i < j:
                T[i][j] = merged[r]
                r += 1
            else:
                T[i][j] = merged[l]
                l += 1
    return

runtests( Median )
