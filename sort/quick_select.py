from utils import *

def quickSelect(A, p, k, idx):
    mid = (p+k)//2
    A[mid], A[k] = A[k], A[mid]
    x = A[k]
    i = p - 1
    for j in range(p, k):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[k] = A[k], A[i+1]

    if i + 1 == idx:
        return x
    elif i + 1 < idx:
        return quickSelect(A, i + 2, k, idx)
    else:
        return quickSelect(A, p, i, idx)

@stats
def wrapper(*args):
    return quickSelect(*args)

arr = randomArray(100, min=0, max=100)
wrapper(arr, 0, len(arr)-1, 49)
