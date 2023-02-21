class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        """Use binary search."""
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif nums[mid] == nums[mid - 1] and mid % 2 == 0:
                right = mid - 1
            elif nums[mid] == nums[mid - 1] and mid % 2 == 1:
                left = mid + 1
            elif nums[mid] == nums[mid + 1] and mid % 2 == 0:
                left = mid + 2
            else:
                right = mid
        return nums[left]
