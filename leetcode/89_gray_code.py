class Solution:
    def gray_code_v1(self, n: int) -> list[int]:
        """Solve by recursion."""

        def recursion(num: int, n: int):
            if n < 0:
                return num
            num = yield from recursion(num, n - 1)
            num ^= (2 ** n)
            yield num
            num = yield from recursion(num, n - 1)
            return num
        return [0] + list(recursion(0, n - 1))

    def gray_code_v2(self, n: int) -> list[int]:
        """Solve by math analysis."""
        return [num ^ (num >> 1) for num in range(0, 2 ** n)]
