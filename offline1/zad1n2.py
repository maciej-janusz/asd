#Maciej Janusz

from zad1testy import runtests

def strong_string(T):
    n=len(T)
    D=[1]*n
    maks = 1
    for i in range(n-2, -1, -1):
        odwr = T[i][::-1]
        for j in range(i+1, n):
            if odwr == T[j] or T[i] == T[j]:
                D[i] += D[j]
                if D[i]>maks:
                    maks = D[i]
                break

    return maks


# Odkomentuj by uruchomic duze testy
runtests( strong_string, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
# runtests( strong_string, all_tests=False )
