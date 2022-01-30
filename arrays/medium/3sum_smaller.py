from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        # sort array to achieve 0 <= i < j < k < n property
        nums.sort()
        result = 0
        # iterate through array till len -2
        for i in range(len(nums) - 2):
            # start find another two numbers by starting new j,k pointers
            # j = next to current
            # k = end of list
            j = i + 1
            k = len(nums) - 1

            # while j and k is not cross each other
            while j < k:
                # get total of three numbers
                tot = nums[i] + nums[j] + nums[k]
                # if sum of three numbers less than target
                if tot < target:
                    # since array is sorted,
                    # we can create triplets that less than target,from all numbers from j to k
                    result += k - j
                    # increase left pointer by one to find another set of triplets
                    j += 1
                # if total is greater than target,we need a smaller total,so to decrease total move right pointer
                else:
                    k -= 1
        return result