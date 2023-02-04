from collections import Counter


class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        """Using counter."""
        counter = Counter(s1)
        cur = Counter(s2[:len(s1)])
        if counter == cur:
            return True

        for drop_ch, ch in zip(s2, s2[len(s1):]):
            cur[drop_ch] -= 1
            cur[ch] += 1
            if counter == cur:
                return True
        return False
