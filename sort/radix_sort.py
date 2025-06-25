from utils import *

def digitisCount(arr):
    maxi = max(arr)
    cnt = 0
    while maxi > 0:
        maxi //= 10
        cnt += 1
    return cnt

def countSort(arr, p):
    cnt = [0]*10
    n = len(arr)

    res = [0]*n
    for i in range(n):
        idx = arr[i]//(p)%10
        cnt[idx] += 1
    for i in range(1, 10):
        cnt[i] += cnt[i-1]

    for i in range(n-1, -1, -1):
        idx = arr[i]//(p)%10
        cnt[idx] -= 1
        res[cnt[idx]] = arr[i]

    return res

@stats
def radixSort(arr):
    digits = digitisCount(arr)
    p = 1
    while p < 10**digits:
        arr = countSort(arr, p)
        p *= 10
    return arr

arr = randomArray(100, min=0, max=10000)
print(radixSort(arr)==sorted(arr))