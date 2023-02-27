# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        node = Node(1, 1, None, None, None, None)
        is_leaf = all(col == grid[0][0] for row in grid for col in row)
        if is_leaf:
            node.val = bool(grid[0][0])
        else:
            node.isLeaf = False
            half = len(grid) // 2
            node.topLeft = self.construct([row[:half] for row in grid[:half]])
            node.topRight = self.construct([row[half:] for row in grid[:half]])
            node.bottomLeft = self.construct([row[:half] for row in grid[half:]])
            node.bottomRight = self.construct([row[half:] for row in grid[half:]])
        return node
