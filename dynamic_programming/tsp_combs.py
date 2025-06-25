import itertools

def tsp(dist):
    n = len(dist)
    memo = {}

    # Base case: cost to reach each city j from 0
    for j in range(1, n):
        memo[(1 << j, j)] = dist[0][j]

    # Iterate subsets of increasing size
    for r in range(2, n):
        for subset in itertools.combinations(range(1, n), r):
            bits = sum([1 << x for x in subset])
            for j in subset:
                prev_bits = bits & ~(1 << j)
                res = []
                for k in subset:
                    if k == j:
                        continue
                    res.append(memo[(prev_bits, k)] + dist[k][j])
                memo[(bits, j)] = min(res)

    # Final step: return to starting city (0)
    bits = (1 << n) - 2  # All except 0
    res = [memo[(bits, j)] + dist[j][0] for j in range(1, n)]
    return min(res)
