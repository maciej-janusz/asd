#Maciej Janusz
'''
  1.Dziele tablice na kubelki o zakresie < D (max-min<D)
  2.Z kazdego kubelka biore min i max
  3.Od aktualnego minimum odejmuje maxa z poprzedniego kubelka i porownuje z D, jak jest >= D zwiekszam licznik,
  O(n+M/D)
'''

from kol1testy import runtests

def ceil(num):
  if num == int(num):
    return int(num)
  return int(num) + 1

def bucket_cnt(arr, M, D):
  n = ceil(M/D)
  buckets = [[] for _ in range(n)]
  for i in range(len(arr)):
    idx = int(arr[i]*n//M)
    buckets[idx].append(arr[i])

  last_max = 0
  cnt = 0
  for i in range(len(buckets)):
    if len(buckets[i]) == 0:
      continue

    mini, maxi = min(buckets[i]), max(buckets[i])

    if mini - last_max >= D:
      cnt += 1
    last_max = maxi
  return cnt

def ogrodzenie(M, D, T):

  return bucket_cnt(T, M, D)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ogrodzenie, all_tests = True )
