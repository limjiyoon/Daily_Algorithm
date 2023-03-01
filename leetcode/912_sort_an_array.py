class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge_sort(left, right):
            """Merge sort"""
            if left +1 >= right:
                return

            mid = left + (right - left) // 2
            merge_sort(left, mid)
            merge_sort(mid, right)

            # merge
            new_arr = [0] * (right - left)
            left_idx, right_idx, new_idx = left, mid, 0
            while left_idx < mid and right_idx < right:
                if nums[left_idx] <= nums[right_idx]:
                    new_arr[new_idx] = nums[left_idx]
                    left_idx += 1
                else:
                    new_arr[new_idx] = nums[right_idx]
                    right_idx += 1
                new_idx += 1

            while left_idx < mid:
                new_arr[new_idx] = nums[left_idx]
                left_idx += 1
                new_idx += 1

            while right_idx < right:
                new_arr[new_idx] = nums[right_idx]
                right_idx += 1
                new_idx += 1

            nums[left:right] = new_arr

        merge_sort(0, len(nums))
        return nums
