import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        """Find the starting point and then search target."""
        # Find the start point before rotation
        start = 0
        for idx, num in enumerate(nums[1:], 1):
            if num < nums[idx - 1]:
                start = idx
                break

        # Search target
        if target <= nums[-1]:
            index = bisect.bisect(nums, target, lo=start, hi=len(nums)) - 1
        else:
            index = bisect.bisect(nums, target, lo=0, hi=start) - 1
        return nums[index] == target

    def search_v2(self, nums: list[int], target: int) -> bool:
        """Find target directly."""
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True

            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        return False
