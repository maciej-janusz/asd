from kol1testy import runtests

def merge(left, right, cnt):
  i, j = 0, 0
  arr = []

  while i < len(left) and j < len(right):
    if left[i][1] < right[j][1]:
      arr.append(left[i])
      i += 1
    else:
      cnt[right[j][0]]+=i
      arr.append(right[j])
      j += 1

  while i < len(left):
    arr.append(left[i])
    i += 1

  while j < len(right):
    cnt[right[j][0]] += i
    arr.append(right[j])
    j += 1

  return arr


def mergesort(arr, cnt):
  n = len(arr)
  if n <= 1:
    return arr
  left = mergesort(arr[:n//2], cnt)
  right = mergesort(arr[n//2:], cnt)
  return merge(left, right, cnt)

def maxrank(T):
  n = len(T)
  tmp = list(enumerate(T))
  cnt = [0] * n
  mergesort(tmp, cnt)
  return max(cnt)



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )