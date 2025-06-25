from utils import *

def partition(A, p, k):
    m = (p+k)//2
    A[m], A[k] = A[k], A[m]
    x = A[k]
    i = p-1
    for j in range(p, k):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    i += 1
    A[i], A[k] = A[k], A[i]
    return i

def quickSort(A, p, k):
    if p < k:
        q = partition(A, p, k)
        quickSort(A, p, q-1)
        quickSort(A, q+1, k)

@timer
def wrapper(*args):
    quickSort(*args)

arr = randomArray(1_000)
wrapper(arr, 0, len(arr)-1)