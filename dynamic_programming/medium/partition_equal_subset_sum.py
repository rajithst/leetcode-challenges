from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target_sum = sum(nums)
        if target_sum % 2 == 1:
            return False

        memo = {}

        def solve(index, remaining):
            if index == -1:
                return remaining == 0
            if remaining == 0:
                return True
            if (index, remaining) in memo:
                return memo[(index, remaining)]

            inc = False
            if remaining - nums[index] >= 0:
                inc = solve(index - 1, remaining - nums[index])
            exc = solve(index - 1, remaining)
            memo[(index, remaining)] = inc or exc
            return inc or exc

        return solve(len(nums) - 1, target_sum / 2)