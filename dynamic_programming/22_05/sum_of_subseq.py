from utils import *

@stats
def min_max_rec(A, K):
    memo = {}

    n = len(A)
    acc_sum = [0]*n
    acc_sum[0] = A[0]
    for i in range(1, n):
        acc_sum[i] = acc_sum[i-1] + A[i]

    def range_sum(i, j):
        if i == 0: return acc_sum[j]
        return acc_sum[j]-acc_sum[i-1]


    def rec(k, i):
        if (k, i) in memo:
          return memo[(k, i)]
        n = len(A)
        if k == 1:
            return range_sum(i, n-1)

        result = 0
        for j in range(i, n-k+1):
            result = max(result, min(range_sum(i, j), rec(k-1, j+1)))

        memo[(k, i)] = result
        return result

    return rec(K, 0)

@stats
def min_max_iter(A, K):
    n = len(A)

    acc_sum = [0] * n
    acc_sum[0] = A[0]
    for i in range(1, n):
        acc_sum[i] = acc_sum[i-1] + A[i]

    def range_sum(i, j):
        if i == 0: return acc_sum[j]
        return acc_sum[j] - acc_sum[i-1]

    dp = [[0] * n for _ in range(K + 1)]

    for i in range(n):
        dp[1][i] = range_sum(i, n - 1)

    for k in range(2, K + 1):
        for i in range(n - k + 1):
            best = 0
            for j in range(i, n - k + 1):
                best = max(best, min(range_sum(i, j), dp[k - 1][j + 1]))
            dp[k][i] = best

    return dp[K][0]


@stats
def min_max_binary_greedy(A, K):
    def can_partition(min_sum):
        count = 0
        current = 0
        for num in A:
            current += num
            if current >= min_sum:
                count += 1
                current = 0
        return count >= K

    low, high = max(A), sum(A)
    result = low

    while low <= high:
        mid = (low + high) // 2
        if can_partition(mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result




k = 10
A = randomArray(1000, min=0, max=1000)

min_max_rec(A, k)
min_max_iter(A, k)
min_max_binary_greedy(A, k)
