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

    def best_team_score_v3(self, scores: list[int], ages: list[int]) -> int:
        """Using binary indexed tree (other's solution)

        Notes:
            Time compleixty: O(NlogN + NlogK)
            Space complexity: O(N + K)
        Reference:
            https://leetcode.com/problems/best-team-with-no-conflicts/solutions/2886659/best-team-with-no-conflicts/
        """
        def query(bit: list[int], idx: int):
            """Query maximum sum before idx."""
            max_score = 0  # Problem constraints: 1 <= score <= 10^6
            while idx > 0:
                max_score = max(max_score, bit[idx])
                idx -= (idx & (-idx))
            return max_score

        def update(bit: list[int], idx: int, value: int) -> None:
            """Add current value to next nodes."""
            bit_len = len(bit)
            while idx < bit_len:
                bit[idx] = max(bit[idx], value)
                idx += (idx & (-idx))

        scores, ages = zip(*sorted(zip(scores, ages)))
        unique_ages = list(set(ages))
        age_to_idx = {age: idx for idx, age in enumerate(sorted(unique_ages), 1)}
        binary_indexed_tree = [0] * (len(age_to_idx) + 1)
        best_score = 0
        for age, score in zip(ages, scores):
            idx = age_to_idx[age]
            cur_best_score = score + query(binary_indexed_tree, idx)
            update(binary_indexed_tree, idx, cur_best_score)
            best_score = max(best_score, cur_best_score)
        return best_score
