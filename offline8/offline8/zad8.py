from zad8testy import runtests

def ice_cream( T ):
    n = len(T)
    buckets = [[] for _ in range(n+1)]
    for i in range(n):
        idx = min(T[i], n)
        buckets[idx].append(T[i])

    cnt = 0
    res = 0
    idx = n
    while idx >= 0:
        for x in buckets[idx]:
            if x - cnt <= 0:
                return res
            else:
                res += x - cnt
                cnt += 1
        idx -= 1


    return res



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )
