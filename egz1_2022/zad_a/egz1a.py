from egz1atesty import runtests

# def snow( S ):
#     n = len(S)
#     memo = {}
#
#     def f(x, y, t):
#         if (x, y, t) in memo:
#             return memo[(x, y, t)]
#
#         if x == y:
#             memo[(x, y, t)] = S[x] - t
#             return S[x] - t
#
#         best = max(f(x+1, y, t+1) + S[x] - t, f(x+1, y, t), f(x, y-1, t+1) + S[y] - t, f(x, y-1, t))
#         memo[(x, y, t)] = best
#         return best
#
#     return f(0, n-1, 0)

def snow(S):
    S_sorted = sorted(S, reverse=True)
    total = 0
    for i in range(len(S_sorted)):
        current = S_sorted[i] - i
        if current > 0:
            total += current
    return total

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
