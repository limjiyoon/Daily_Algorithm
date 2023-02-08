from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotate_right_v1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Over time requirement if k is too large."""
        if not head or not head.next or k == 0:
            return head

        mid = head
        for _ in range(k):
            mid = mid.next if mid.next else head

        if mid == head:
            return head

        last = head
        while mid.next:
            mid = mid.next
            last = last.next

        mid.next = head
        head, last.next = last.next, None
        return head

    def rotate_right_v2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Solve with two pointer method and pre-calculate length."""
        if not head or not head.next or k == 0:
            return head

        length = 1
        cur = head
        while cur.next:
            cur = cur.next
            length += 1
        k = k % length

        if k == 0:
            return head

        mid = head
        for _ in range(k):
            mid = mid.next

        last = head
        while mid.next:
            mid = mid.next
            last = last.next

        mid.next = head
        head, last.next = last.next, None
        return head
