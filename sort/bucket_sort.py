from utils import *

def bucket_sort(arr, a, b):
    n = len(arr)
    if n <= 1:
        return arr
    buckets = [[] for _ in range(n)]
    for i in range(n):
        idx = int((arr[i]-a)*n//(b - a))
        buckets[idx].append(arr[i])
    ret = []
    for i in range(n):
        ret.extend(sorted(buckets[i]))
    return ret

@stats
def wrapper(*args):
    return bucket_sort(*args)

arr = randomArray(10, min=0.5, max=1, floating=True)
wrapper(arr, 0.5, 1)