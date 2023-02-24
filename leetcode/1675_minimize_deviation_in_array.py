from heapq import heappop, heappush, heapify
class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        """Solve with heap and greedy method."""
        heap: list[tuple[int, int]] = []
        for idx, num in enumerate(nums):
            while num % 2 == 0:
                num //= 2
            heap.append((num, max(nums[idx], num * 2)))

        dev = max_v = max(heap)[0]
        heapify(nums)

        cur, bound = 0, 1  # For initialize condition.
        while cur < bound:
            cur, bound = heappop(heap)
            dev = min(dev, max_v - cur)

            if cur < bound:
                max_v = max(max_v, cur * 2)
                heappush(heap, (cur * 2, bound))

        return dev
