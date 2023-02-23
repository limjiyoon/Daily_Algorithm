from heapq import heappush, heappop

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        heap = []
        projects = sorted(zip(capital, profits))
        cur_idx = 0
        for _ in range(k):
            while cur_idx < len(projects) and projects[cur_idx][0] <= w:
                heappush(heap, -projects[cur_idx][1])
                cur_idx += 1
            if heap:
                w -= heappop(heap)
        return w
