class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        longer = str1
        smaller = str2

        while len(longer) != len(smaller):
            if len(longer) < len(smaller):
                longer, smaller = smaller, longer

            for smaller_ch, longer_ch in zip(smaller, longer):
                if smaller_ch != longer_ch:
                    return ""
            smaller, longer = longer[len(smaller):], smaller

        return smaller if longer == smaller else ""
