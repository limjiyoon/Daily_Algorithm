from itertools import groupby, product


class Solution:
    def subsets_without_dup(self, nums: list[int]) -> list[list[int]]:
        """Solve by backtracking.

        Notes:
            Given a collection of integers that might contain duplicates.
        """
        group_subsets = []
        nums.sort()
        for num, group in groupby(nums):
            group_subset: list[list[int]] = [[]]
            for _ in group:
                group_subset.append(group_subset[-1] + [num])
            group_subsets.append(group_subset[1:])

        subsets: list[list[int]] = [[]]
        for other_subset in group_subsets:
            for subset_1, subset_2 in product(subsets, other_subset):
                subsets.append(subset_1 + subset_2)
        return subsets
