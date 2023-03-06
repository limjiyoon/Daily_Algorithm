class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        start, end = 0, len(arr)
        while start < end:
            mid = start + (end - start) // 2
            if arr[mid] > mid + k:
                end = mid
            else:
                start = mid + 1
        return end + k
