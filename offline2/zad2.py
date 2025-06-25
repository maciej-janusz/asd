from zad2testy import runtests

def merge(left, right, cnt):
    i = 0
    j = 0
    B = []
    nl = len(left)
    nr = len(right)
    while i < nl and j < nr:
        if left[i] <= right[j]:
            B.append(left[i])
            i += 1
        else:
            B.append(right[j])
            j += 1
            cnt += nl - i

    B.extend(left[i:])
    B.extend(right[j:])
    return B, cnt

def merge_count(A):
    n = len(A)
    if n <= 1:
        return A, 0

    mid = n//2
    left, cntl = merge_count(A[:mid])
    right, cntr = merge_count(A[mid:])
    return merge(left, right, cntl+cntr)
def count_inversions(A):
    return merge_count(A)[1]


# Odkomentuj by uruchomic duze testy
runtests( count_inversions, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
# runtests( count_inversions, all_tests=False )
