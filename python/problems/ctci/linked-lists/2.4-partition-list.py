"""
Partition: Write code to partition a linked list around a value x, such that 
all nodes less than x come before all nodes greater than or equal to x. 
If x is contained within the list the values of x only need to be after the 
elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.

EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""
from typing import Optional
import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def partition(head: Optional[ListNode], x: int) -> ListNode:
    left, right = ListNode(), ListNode()  # dummy nodes to start
    left_tail, right_tail = left, right

    # partition
    while head:
        # partition, left is strictly less than x
        if head.val < x:
            left_tail.next = head
            left_tail = left_tail.next
        else:
            right_tail.next = head
            right_tail = right_tail.next
        head = head.next

    # connect the left and right
    # right is a dummy node, so right.next is first real node
    left_tail.next = right.next
    # last node (right_tail is currently pointing to a node, we need it to point to null)
    right_tail.next = None

    return left.next
