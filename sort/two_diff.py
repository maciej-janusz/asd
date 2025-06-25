def twoDiff(tab, x):
    n = len(tab)
    i = 0
    j = 1
    while i < n and j < n:
        r = tab[j] - tab[i]
        if r == x:
            return i, j
        elif r < x:
            j += 1
        else:
            i += 1
    return -1, -1
