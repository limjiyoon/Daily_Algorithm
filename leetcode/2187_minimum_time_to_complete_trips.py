class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        start = min(time)
        end = start * totalTrips

        while start < end:
            mid = start + (end - start) // 2
            n_trips = sum(mid // t for t in time)
            if n_trips >= totalTrips:
                end = mid
            else:
                start = mid + 1
        return start

