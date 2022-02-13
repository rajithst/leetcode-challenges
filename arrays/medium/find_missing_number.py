from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        i = 0
        n = len(nums)
        # using cyclic sort
        while i < n:
            # correct index for value
            j = nums[i]

            # if j is less than n (because indexes goes up to n-1) and current value is not in correct index
            # swap values
            if j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            # current value in correct index,go to next pointer
            else:
                i += 1

        # find the missing value in this sorted array
        for i in range(n):
            if nums[i] != i:
                return i
        return n