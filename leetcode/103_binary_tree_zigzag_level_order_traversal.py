from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """BFS with queue and reverse"""
        if not root:
            return []

        queue = [root]
        values = []
        start_left = True
        while queue:
            values.append([node.val for node in queue])
            new_queue = []
            for node in queue:
                if start_left and node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
                if not start_left and node.left:
                    new_queue.append(node.left)
            queue = new_queue[::-1]
            start_left = not start_left
        return values
