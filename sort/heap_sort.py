from utils import *

def left(i):
    return 2*i+1
def right(i):
    return 2*i+2
def parent(i):
    return (i-1)//2

def heapify(arr, n, i):
    max_idx = i
    l = left(i)
    r = right(i)
    if l < n and arr[l] > arr[max_idx]:
        max_idx = l
    if r < n and arr[r] > arr[max_idx]:
        max_idx = r

    if max_idx != i:
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        heapify(arr, n, max_idx)

def buildHeap(arr):
    n = len(arr)
    for i in range(parent(n-1), -1, -1):
        heapify(arr, n, i)

@timer
def heapSort(_arr):
    arr = _arr[:]

    n = len(arr)
    buildHeap(arr)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


arr = randomArray(1_000_000)

heapSort(arr)