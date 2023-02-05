class Solution:
    def insert_v1(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        """Naive solution."""
        intervals.append([100_001, 100_001])
        new_start, new_end = newInterval
        updated_intervals = []
        for idx, (start, end) in enumerate(intervals):
            if new_start > end:
                updated_intervals.append([start, end])
            if new_end < start:
                updated_intervals.append([new_start, new_end])
                updated_intervals.extend(intervals[idx:-1])
                break
            if start < new_start <= end:
                new_start = start
            if start <= new_end < end:
                new_end = end
        return updated_intervals

    def insert_v2(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        """Refactor version 1."""
        left = []
        right = []
        new_start, new_end = new_interval
        for start, end in intervals:
            if end < new_start:
                left.append([start, end])
            elif start > new_end:
                right.append([start, end])
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)
        return left + [[new_start, new_end]] + right
