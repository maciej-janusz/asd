from egz3btesty import runtests


def bisearch(arr, start_idx, a, b):
    l = start_idx
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        c, d, idx = arr[mid]

        sep = b < c or d < a
        incl = (a <= c and d <= b) or (c <= a and b <= d)

        if not sep and not incl:
            return idx

        if c <= a or d <= b:
            l = mid + 1
        else:
            r = mid - 1

    return -1

def uncool( P ):
  n = len(P)
  P = [(P[i][0], P[i][1], i)  for i in range(n)]
  P.sort()

  for i in range(n):
    a, b, idx = P[i]
    res = bisearch(P, i+1, a, b)
    if res != -1:
      return (idx, res)

  return -1



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True )
