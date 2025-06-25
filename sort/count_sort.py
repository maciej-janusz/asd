from utils import *

@stats
def countSort(A, a, b):
    b += 1
    n = len(A)
    k = b-a
    C = [0] * k
    B = [0] * n

    for i in range(n):
        C[A[i]-a] += 1
    for i in range(1, k):
        C[i] += C[i-1]

    for i in range(n-1, -1, -1):
        C[A[i]-a] -= 1
        B[C[A[i]-a]] = A[i]
    return B

arr = randomArray(100, min=-100, max=100)
countSort(arr, -100, 100)