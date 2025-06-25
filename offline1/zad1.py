#Maciej Janusz
'''
    1.Odwracamy czesc wyrazow tak aby wszystkie byly odwrocone wedlug jednego schematu (jak najmniejsze leksykograficznie)
    2.Sortujemy tablice, zeby takie same wyrazy byly obok siebie
    3.Zliczamy ile jest takich samych wyrazow obok siebie
    czasowa: O(N) + O(nlogn) + O(n) = O(N + nlogn)
    pamieciowa: O(n)
'''
from zad1testy import runtests


def merge(left, right):
    n1 = len(left)
    n2 = len(right)
    i = 0
    j = 0
    T = []

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            T.append(left[i])
            i += 1
        else:
            T.append(right[j])
            j += 1

    T.extend(left[i:])
    T.extend(right[j:])

    return T


def merge_sort(T):
    n = len(T)
    if n <= 1:
        return T

    mid = n//2
    left = merge_sort(T[:mid])
    right = merge_sort(T[mid:])

    return merge(left, right)


def strong_string(T):
    n=len(T)

    for i in range(n):
        rev = T[i][::-1]
        if rev < T[i]:
            T[i] = rev

    T = merge_sort(T)

    prev = T[0]
    cnt = 1
    maxi = 1
    for i in range(1, n):
        if prev == T[i]:
            cnt += 1
            if cnt > maxi:
                maxi = cnt

        else:
            cnt = 1
            prev = T[i]

    return maxi


# Odkomentuj by uruchomic duze testy
runtests( strong_string, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
# runtests( strong_string, all_tests=False )
