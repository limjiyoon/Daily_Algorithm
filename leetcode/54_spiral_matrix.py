from typing import Generator
class Solution:
    def spiral_order_v1(self, matrix: list[list[int]]) -> list[int]:
        """Using generator for simulating spiral order."""
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        return [matrix[row][col] for col, row in self.spiral_order_index(n_rows, n_cols)]

    def spiral_order_index(
        self,
        n_rows: int,
        n_cols: int
    ) -> Generator[list[int], None, None]:
        """Calculate index of spiral order."""
        coord = [-1, 0]
        remain = [n_cols, n_rows - 1]
        axis, move = 0, 1
        while remain[axis] > 0:
            for _ in range(remain[axis]):
                coord[axis] += move
                yield coord
            remain[axis] -= 1
            move *= 1 if axis == 0 else -1
            axis ^= 1  # 0 -> 1, 1 -> 0
