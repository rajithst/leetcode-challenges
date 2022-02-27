from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        all_subsets = [[]]

        # add empty array as first subset

        # iterate over numbers and create new subsets from available subsets
        for current_number in nums:

            # create new subset by adding current number to all available subsets

            available_subsets = len(all_subsets)
            for i in range(available_subsets):
                new_subset = all_subsets[i].copy()
                new_subset.append(current_number)
                all_subsets.append(new_subset)
        return all_subsets
