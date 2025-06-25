from zad3testy import runtests

def bisearch(P, x, l, r):
    while l < r:
        mid = (r + l) // 2
        if P[mid][0] <= x <= P[mid][1]:
            return mid
        elif P[mid][0] > x:
            r = mid - 1
        else:
            l = mid + 1

    return l

def insert_sort(T, cmp = lambda x: x):
    for i in range(len(T)):
        tmp = T[i]
        j = i - 1
        while j >= 0 and cmp(T[j]) > cmp(tmp):
            T[j+1] = T[j]
            j -= 1
        T[j+1] = tmp

cmp_range = lambda x: x[0]

def SortTab(T,P):
    #sortowanie przedzialow
    insert_sort(P, cmp_range)
    #ucinanie przedzialow
    for i in range(1, len(P)):
        if P[i-1][1] > P[i][0]:
            if P[i-1][2] <= P[i][2]:
                P[i] = (P[i-1][1], P[i][1], P[i][2])
            else:
                P[i-1] = (P[i-1][0], P[i][0], P[i-1][2])
    #rozdzielam liste na przedzialy
    D = [[] for _ in range(len(P))]
    for x in T:
        D[bisearch(P, x, 0, len(P))].append(x)

    #sortujemy i mergujemy
    i = 0
    for j in range(len(D)):
        insert_sort(D[j])
        for item in D[j]:
            T[i] = item
            i += 1
    return

runtests( SortTab )
