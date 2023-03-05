from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        same_val_idx = defaultdict(list)
        for idx, val in enumerate(arr):
            same_val_idx[val].append(idx)

        jump = 0
        queue, visit = deque([(0, 0)]), {-1}

        while queue:
            idx, jump = queue.popleft()
            if idx == len(arr) - 1:
                break

            for nxt_idx in [idx - 1, idx + 1] + same_val_idx[arr[idx]]:
                if nxt_idx not in visit and nxt_idx != idx:
                    queue.append([nxt_idx, jump + 1])
                    visit.add(nxt_idx)
            same_val_idx[arr[idx]] = []

        return jump
