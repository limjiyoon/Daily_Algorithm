class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        """Solve with binary search."""
        left, right = max(weights), sum(weights) + 1

        def is_possible(max_load: int) -> bool:
            """Check the possibility of shipping the loads within the days and given max load."""
            cur_days = 1
            cur_load = 0
            for weight in weights:
                cur_load += weight
                if cur_load > max_load:
                    cur_days += 1
                    cur_load = weight
            return cur_days <= days

        while left < right:
            mid = left + (right - left) // 2
            if is_possible(max_load=mid):
                right = mid
            else:
                left = mid + 1
        return left
