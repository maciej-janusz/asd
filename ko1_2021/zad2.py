from zad2testy import runtests

class Node:
  def __init__(self):
    self.val = None
    self.next = None


def mergesort(p):
    if not p or not p.next:
        return p
    left = p
    slow = p
    fast = p
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = None
    left = mergesort(left)
    right = mergesort(slow)

    merged = Node()
    ret = merged
    while left and right:
        if left.val <= right.val:
            merged.next = left
            left = left.next
        else:
            merged.next = right
            right = right.next
        merged = merged.next
    if left:
        merged.next = left
    if right:
        merged.next = right
    return ret.next



def SortH(p,k):
    p = mergesort(p)
    return p


runtests( SortH )
