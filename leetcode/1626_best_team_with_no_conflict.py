# python 3.11
class Solution:

    def best_team_score_v1(self, scores: list[int], ages: list[int]) -> int:
        """Naive Solution (Bruth Force).

        Notes:
            Time Complexity: O(2^N)
            Space Complexity: O(N)  # Maximum number of call stacks
        """
        # Sort lower ages, lower scores first
        # Then it becomes a problem to find a increasing sequence with maximum sum
        _, scores = zip(*sorted(zip(ages, scores)))

        def best_with_constraint(idx, lower_bound_score):
            if idx == len(scores):
                return 0
            without = best_with_constraint(idx + 1, lower_bound_score)
            if scores[idx] < lower_bound_score:
                return without
            return max(
                scores[idx] + best_with_constraint(idx + 1, scores[idx]),
                without
            )
        return best_with_constraint(0, 0)

    def best_team_score_v2(self, scores: list[int], ages: list[int]) -> int:
        """Using dynamic programming

        Notes:
            Time compleixty: O(N^2)
            Space complexity: O(N)
        """
        scores = [score for _, score in sorted(zip(ages, scores))]
        max_seq = scores[:]

        for cur_idx, cur_value in enumerate(scores):
            for prev_idx in range(cur_idx):
                if (cur_value >= scores[prev_idx] and
                    max_seq[cur_idx] < max_seq[prev_idx] + cur_value):
                    max_seq[cur_idx] = max_seq[prev_idx] + cur_value
        return max(max_seq)
