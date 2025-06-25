from utils import *

def hoare(arr, l, r):
    pivot = arr[l]
    l -= 1
    r += 1

    while True:
        l += 1
        while arr[l] < pivot:
            l += 1

        r -= 1
        while arr[r] > pivot:
            r -= 1

        if l >= r:
            return r

        arr[l], arr[r] = arr[r], arr[l]

def quick_sort_hoare(arr, l, r):
    if l < r:
        q = hoare(arr, l, r)
        quick_sort_hoare(arr, l, q)
        quick_sort_hoare(arr, q+1, r)

arr = randomArray(100)
quick_sort_hoare(arr, 0, 99)
print(arr)