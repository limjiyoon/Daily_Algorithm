from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """Use left, right to store the nodes smaller and larger than x."""
        left = ListNode()
        left_cur = left
        right = ListNode()
        right_cur = right

        while head:
            if head.val >= x:
                right_cur.next = head
                right_cur = right_cur.next
            else:
                left_cur.next = head
                left_cur = left_cur.next
            head = head.next
        right_cur.next = None
        left_cur.next = right.next
        return left.next
