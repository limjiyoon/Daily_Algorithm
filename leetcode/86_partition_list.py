from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition_v1(
        self,
        head: Optional[ListNode],
        target: int
    ) -> Optional[ListNode]:
        """Use left, right to store the nodes smaller and larger than x."""
        left = ListNode()
        left_cur = left
        right = ListNode()
        right_cur = right

        while head:
            if head.val >= target:
                right_cur.next = head
                right_cur = right_cur.next
            else:
                left_cur.next = head
                left_cur = left_cur.next
            head = head.next
        right_cur.next = None
        left_cur.next = right.next
        return left.next

    def partition_v2(
        self,
        head: Optional[ListNode],
        target: int
    ) -> Optional[ListNode]:
        """Push the nodes larger than x to the end of the list."""
        if not head:
            return head

        last = head
        length = 1
        while last.next:
            last = last.next
            length += 1

        cur = dummy_head = ListNode(next=head)
        for _ in range(length):
            if cur.next.val >= target:
                last.next = cur.next
                cur.next = cur.next.next
                last = last.next
                last.next = None
            else:
                cur = cur.next
        return dummy_head.next
