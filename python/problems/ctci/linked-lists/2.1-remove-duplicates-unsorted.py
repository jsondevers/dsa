from typing import Optional
import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Time: O(n), Space: O(n)
def remove_dups(head: Optional[ListNode]):
    if head.head is None:
        return

    current = head.head
    seen = set([current.value])
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next

    return head


# Time: O(n^2), Space: O(1)
def remove_dups_followup(head):
    if head.head is None:
        return

    current = head.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return head.head


def print_list(head: Optional[ListNode]):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    res.append(None)
    print(res)


class Test(unittest.TestCase):
    head = ListNode(0)
    curr = head

    for i in range(1, 10):
        curr.next = ListNode(i)
        curr = curr.next
        if i % 2:
            curr.next = ListNode(i)
            curr = curr.next
    print_list(curr)
    ansHead = ListNode(0)
    ans = ansHead
    for i in range(1, 10):
        ans.next = ListNode(i)
        ans = ans.next
    print_list(ans)
