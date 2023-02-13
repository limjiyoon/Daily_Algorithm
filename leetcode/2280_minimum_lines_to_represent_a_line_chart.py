class Solution:
    def minimumLines(self, stockPrices: list[list[int]]) -> int:
        """Solves the problem with greedy algorithm.

        Notes:
            I use two tricks to solve this problem.
            1. Set initial delta value of x as 0 since x value is unique.
            2. Calculate slope of each line by multiplication since division
               may cause precision error.
        """
        n_lines = 0
        prev_dx, prev_dy = 0, 1  # There is no case that dx is 0

        stockPrices.sort()
        for prev, cur in zip(stockPrices, stockPrices[1:]):
            cur_dx, cur_dy = cur[0] - prev[0], cur[1] - prev[1]
            if prev_dx * cur_dy != prev_dy * cur_dx:
                n_lines += 1
                prev_dx, prev_dy = cur_dx, cur_dy
        return n_lines
