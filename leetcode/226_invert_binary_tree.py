from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invert_tree_v1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Solve with recursion"""
        if not root:
            return root

        root.left, root.right = self.invert_tree_v1(root.right), self.invert_tree_v1(root.left)
        return root

    def invert_tree_v2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Solve with stack"""
        if not root:
            return root

        stack = [root]
        while stack:
            cur = stack.pop()
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return root
