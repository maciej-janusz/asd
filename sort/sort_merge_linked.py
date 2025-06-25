from utils import *
from linked import *


def merge(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    head = Node()
    ret = head
    while l1 and l2:
        if l1.val <= l2.val:
            head.next = l1
            head = head.next
            l1 = l1.next
        else:
            head.next = l2
            head = head.next
            l2 = l2.next

    if l1:
        head.next = l1
    if l2:
        head.next = l2

    return ret.next


def series(head):
    if head is None:
        return None
    curr = head
    first = curr
    second = None
    third = None
    while curr.next is not None:
        if curr.val <= curr.next.val:
            curr = curr.next
        else:
            tmp = curr.next
            curr.next = None
            curr2 = tmp
            second = curr2
            while curr2.next is not None:
                if curr2.val <= curr2.next.val:
                    curr2 = curr2.next
                else:
                    tmp = curr2.next
                    curr2.next = None
                    third = tmp
    return (first, second, third)


def sort(head):
    if head is None:
        return None
    first, second, third = series(head)
    while third is not None:
        head = merge(first, second)
        ptr = head
        while head.next is not None:
            head = head.next
        head.next = third
        first, second, third = series(ptr)

    return merge(first, second)


l1 = arrayToLinked(randomArray(100))

res = sort(l1)
print(linkedToArray(res))
