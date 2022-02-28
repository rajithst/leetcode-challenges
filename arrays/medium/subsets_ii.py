from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # sort numbers to identify duplicate numbers easily
        nums.sort()
        all_subsets = [[]]

        # add empty array as first subset

        endIndex = 0
        # iterate over numbers and create new subsets from available subsets
        for j in range(len(nums)):
            # every iteration,we try to create subsets from all available subsets
            startIndex = 0

            # if previous number is same as current number(duplicate number)
            # we only need to create subsets from previous step outputs
            #  --- since number is duplicated,all the subsets are already in the results except previous step
            # so we change startIndex to skip all old subsets
            # endIndex is always pointing to end of the results array
            # so when we have a duplicate number,startIndex should be end of previous step
            # which is endIndex before update in current iteration
            if j > 0 and nums[j] == nums[j - 1]:
                startIndex = endIndex + 1
            # create new subset by adding current number to all available subsets
            endIndex = len(all_subsets) - 1
            for i in range(startIndex, endIndex + 1):
                new_subset = all_subsets[i].copy()
                new_subset.append(nums[j])
                all_subsets.append(new_subset)
        return all_subsets
