#Maciej Janusz
"""
    Funckcja rekurencyjna ze spamietywaniem szukamy minimalnej liczby ciec, sprawdzajac wszytskie mozliwe
    blaty pozostałe po odcięciu kolejnych desek.

    f(x, y) - minimalna liczba ciec na blacie w ktorym odcieto y metrow od gory i x metrow od lewej
    f(m-1, n-1) = 0 - jesli blat jest poprawna deska, inf - w przeciwnym razie
    f(x, y) =   0 - jesli blat jest poprawna deska
                min{f(x, y+1) + 1 [jezeli mozemy odciac z gory], f(x+1, y) + 1 [jezeli mozemy odciac z lewej], inf} - w przeciwnym razie
    wynikiem jest f(0, 0) [pelny blat], lub -1 jak f(0, 0) zwroci inf

    O(nm)
"""
from kol3testy import runtests
from math import inf

def parkiet(B, C, s):
    n = len(B)
    m = len(B[0])
    memo = {}

    def f(x, y):
        if (x, y) in memo:
            return memo[(x, y)]

        res = inf
        if y == n-1 or x == m-1:
            if C[y][x] <= s:
                res = 0
            elif y == n-1:
                res = min(res, f(x+1, y)+1)
            elif x == m-1:
                res = min(res, f(x, y+1)+1)
        else:
            if C[y][x]-C[y][x+1] <= s:
                res = min(res, f(x+1, y)+1)
            if C[y][x]-C[y+1][x] <= s:
                res = min(res, f(x, y+1)+1)

        memo[(x, y)] = res
        return res

    ret = f(0, 0)
    if ret == inf:
        return -1
    else:
        return ret


def parkiet_greedy(B, C, s):
    n = len(B)
    m = len(B[0])
    cnt_x = 0
    cnt_y = 0

    for i in range(n):
        C[i].append(0)
    C.append([0]*m)

    #tniemy wszyskie pionowo
    x = 0
    y = 0
    while x < m:
        if C[y][x] - C[y][x+1] > s:
            y += 1
            cnt_y += 1
        else:
            x += 1

    # tniemy wszyskie poziomo
    x = 0
    y = 0
    while y < n:
        if C[y][x] - C[y+1][x] > s:
            x += 1
            cnt_x += 1
        else:
            y += 1

    return min(cnt_x + n, cnt_y + m)-1



runtests(parkiet_greedy, all_tests = True)
