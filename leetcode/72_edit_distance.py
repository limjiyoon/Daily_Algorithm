class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        dp = list(range(len(word2) + 1))

        for word1_idx in range(len(word1)):
            prev, dp[0] = word1_idx, word1_idx + 1
            for word2_idx in range(len(word2)):
                prev, dp[word2_idx + 1] = dp[word2_idx + 1], min(
                    prev + int(word1[word1_idx] != word2[word2_idx]),
                    dp[word2_idx] + 1,
                    dp[word2_idx + 1] + 1
                )

        return dp[-1]
