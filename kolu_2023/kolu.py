from kolutesty import runtests



def ice_cream( T ):
    T.sort(key=lambda x: -x)
    n = len(T)
    i = 0
    cnt = 0
    res = 0
    while i < n:
        if T[i]-cnt <= 0:
            i += 1
            continue
        res += T[i]-cnt
        i += 1
        cnt += 1

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )