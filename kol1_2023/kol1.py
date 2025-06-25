from kol1testy import runtests

left = lambda i: 2*i+1
right = lambda i: 2*i+2
parent = lambda i: (i-1)//2


def heapify_min_up(arr, i):
    idx = parent(i)
    if i > 0 and arr[i][1] < arr[idx][1]:
        arr[idx], arr[i] = arr[i], arr[idx]
        heapify_min_up(arr, idx)
def heapify_min_down(arr, i, n):
    min_idx = i
    l = left(i)
    r = right(i)
    if l < n and arr[l][1]<arr[min_idx][1]:
        min_idx = l
    if r < n and arr[r][1]<arr[min_idx][1]:
        min_idx = r
    if min_idx != i:
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
        heapify_min_down(arr, min_idx, n)

def build_min_heap(arr, n):
    for i in range(parent(n-1), -1, -1):
        heapify_min_down(arr, i,  n)

def pop(arr):
    ret = arr[0]
    last = arr.pop()
    arr[0] = last
    heapify_min_down(arr, 0, len(arr))
    return ret

def push(arr, item):
    arr.append(item)
    heapify_min_up(arr, len(arr)-1)

def ksum(T, k, p):
    n = len(T)
    T = list(enumerate(T))
    arr = T[:k]
    build_min_heap(arr, k)
    for i in range(p-k):
        if arr[0][1] < T[k+i][1]:
            arr[0] = T[k+i]
            heapify_min_down(arr, i, len(arr))
    res = arr[0][1]
    for i in range(p, n):
        while arr[0][0] <= i - p:
            pop(arr)
        push(arr, T[i])
        res += arr[0][1]

    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
