from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
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
