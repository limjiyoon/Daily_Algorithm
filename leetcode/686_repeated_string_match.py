class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """Naive check for each possible number of repeats"""
        lower_bound = -(-len(b) // len(a))  # ceil of a / b
        for repeats in range(lower_bound, lower_bound + 2):
            if b in a * repeats:
                return repeats
        return - 1

    def repeated_string_match(self, a: str, b: str) -> int:
        """Use KMP Algorithm."""
        def kmp_table(s: str) -> list[int]:
            """Return the KMP table for the given string."""
            table = [0] * len(s)
            for i in range(1, len(s)):
                j = table[i - 1]
                while j > 0 and s[i] != s[j]:
                    j = table[j - 1]
                if s[i] == s[j]:
                    j += 1
                table[i] = j
            return table

        def kmp_search(s: str, p: str) -> int:
            """Return the index of the first match of p in s, or -1 if not found."""
            table = kmp_table(p)
            i = j = 0
            while i < len(s):
                if s[i] == p[j]:
                    i += 1
                    j += 1
                    if j == len(p):
                        return i - j
                elif j > 0:
                    j = table[j - 1]
                else:
                    i += 1
            return -1

        # KMP search for b in a
        index = kmp_search(a, b)
        if index != -1:
            return 1

        # KMP search for b in a + a
        index = kmp_search(a + a, b)
        if index != -1:
            return 2

        return -1
