from typing import Optional
import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Iterative: Time: O(n), Space: O(1)
def remove_dups(head: Optional[ListNode], k: int):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next

    return dummy.next


# Recursive: Time: O(n), Space: O(n)
