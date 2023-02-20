import bisect


class Solution:
    def search_insert_v1(self, nums: list[int], target: int) -> int:
        """Implement binary search."""
        start, end = 0, len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start

    def search_insert_v2(self, nums: list[int], target: int) -> int:
        """Use bisect stl module."""
        return bisect.bisect_left(nums, target)
