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

    def spiral_order_v2(self, matrix: list[list[int]]) -> list[int]:
        """Using recursive."""
        # https://github.com/python/cpython/blob/a62be77266b1beadd42d4952186332bc0847b7d6/Objects/listobject.c#L465
        # cur_line = [*matrix[0]]  # Time complexity O(N), Space compleixty: O(N)

        cur_line = [*matrix.pop(0)]  # Time complexity O(N), Space complexity: O(1)

        # Below line38 is same as follows:
        # next_lines = []
        # if matrix:
        #     rotate_matrix = [*zip(*matrix)]
        #     next_lines = self.spiral_order_v2(rotate_matrix[::-1])
        next_lines = matrix and self.spiral_order_v2([*zip(*matrix)][::-1])
        return cur_line + next_lines
