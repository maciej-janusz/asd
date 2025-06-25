def get_items(arr, P, F, max_l):
    n = len(arr)
    idx = F.index(max_l)
    items = [idx]

    while P[idx] is not None:
        idx = P[idx]
        items.append(idx)

    return items[::-1]

def lis(arr):
    n = len(arr)
    F = [1]*n
    P = [None]*n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                if F[j]+1 > F[i]:
                    F[i] = F[j]+1
                    P[i] = j

    max_l = max(F)
    return max_l, get_items(arr, P, F, max_l)

arr = [0, 3, 2, 10, 15, 8, 64]
print(lis(arr))