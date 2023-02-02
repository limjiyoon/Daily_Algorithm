class Solution:
    def is_alien_sorted(self, words: list[str], order: str) -> bool:
        """Compare with sorted words.

        Notes:
            Time complexity: O(NMlogN)
            - N: len(words)
            - M: max(len(word))
        """
        to_idx = dict(zip(order, range(len(order))))
        idx_words = [[to_idx[ch] for ch in word] for word in words]
        return idx_words == sorted(idx_words)

    def is_alien_sorted_v2(self, words: list[str], order: str) -> bool:
        """Compare neighbor words only.

        Notes:
            Time complexity: O(NM)
        """
        to_idx = {ch: idx for idx, ch in enumerate(order)}
        idx_words = [[to_idx[ch] for ch in word] for word in words]
        return all(cur <= nxt for cur, nxt in zip(idx_words, idx_words[1:]))
