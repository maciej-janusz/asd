from utils import *


@timer
def insSort(arr):
    n = len(arr)
    for i in range(1, n):
        tmp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = tmp
    return arr

arr = randomArray(1_000_000)

insSort(arr)