class Solution:
    def grayCode(self, n: int) -> list[int]:
        """Solve by recursion."""

        def dp(num: int, n: int):
            if n < 0:
                return num
            num = yield from dp(num, n - 1)
            num ^= (2 ** n)
            yield num
            num = yield from dp(num, n - 1)
            return num
        return [0] + list(dp(0, n - 1))
