from linked import *

def revLinked(head):
    curr = head
    prev = None
    while curr is not None:
        tmp_next = curr.next
        curr.next = prev
        prev = curr
        curr = tmp_next

    return prev


tab = [1, 2, 3, 4, 5]
head = arrayToLinked(tab)
print(linkedToArray(revLinked(head)))
