class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def ceil(value: int, divisor: int):
            return -(-value // divisor)

        start, end = 1, max(piles)
        while start < end:
            mid = start + (end - start) // 2

            duration = sum(ceil(pile, mid) for pile in piles)
            if duration <= h:
                end = mid
            else:
                start = mid + 1
        return end
