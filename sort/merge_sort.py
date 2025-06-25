from utils import *


def merge(left, right):
    res = []

    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append((right[j]))
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return res

def mergeSort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    mid = n//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)


@timer
def wrapper(*args):
    return mergeSort(*args)

arr = randomArray(1_000_000)
wrapper(arr)