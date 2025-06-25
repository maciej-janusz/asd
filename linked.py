from typing import Optional, List


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def arrayToLinked(tab: List):
    head = Node()
    curr = head
    n = len(tab)
    for i in range(n):
        curr.val = tab[i]
        if i < n-1:
            curr.next = Node()
            curr = curr.next

    return head


def linkedToArray(head: Optional[Node]):
    curr = head
    tab = []
    while curr is not None:
        tab.append(curr.val)
        curr = curr.next
    return tab

