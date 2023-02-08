class Solution:
    def remove_duplicates(self, nums: list[int]) -> int:
        """Increase index if the number is greater than the previous number."""
        idx = 2
        for num in nums[2:]:
            if num > nums[idx - 2]:
                nums[idx] = num
                idx += 1
        return min(len(nums), idx)
