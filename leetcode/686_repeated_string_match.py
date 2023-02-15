class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """Naive check for each possible number of repeats"""
        lower_bound = -(-len(b) // len(a))  # ceil of a / b
        for repeats in range(lower_bound, lower_bound + 2):
            if b in a * repeats:
                return repeats
        return - 1
