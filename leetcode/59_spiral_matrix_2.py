from typing import Generator


class Solution:
    def generate_matrix(self, n: int) -> list[list[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for idx, (row, col) in enumerate(self.spiral_order(n), 1):
            matrix[row][col] = idx
        return matrix

    def spiral_order(self, n: int) -> Generator[tuple[int, int], None, None]:
        """Generate spiral order."""
        row, col = -1, -1
        size = n
        while size > 1:
            row += 1
            col += 1
            for _ in range(size - 1):
                yield row, col
                col += 1
            for _ in range(size - 1):
                yield row, col
                row += 1
            for _ in range(size - 1):
                yield row, col
                col -= 1
            for _ in range(size - 1):
                yield row, col
                row -= 1
            size -= 2

        if size > 0:
            yield n // 2, n // 2

    def generate_matrix_v2(self, n: int) -> list[list[int]]:
        """Use python trick."""
        matrix, low = [[n*n]], n * n
        while low > 1:
            low, high = low - len(matrix), low
            matrix = [list(range(low, high))] + list(zip(*matrix[::-1]))
        return matrix
