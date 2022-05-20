from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}

        def solve(index, remaining):
            if index == len(nums):
                if remaining == target:
                    return 1
                else:
                    return 0

            if (index, remaining) in memo:
                return memo[(index, remaining)]

            # every value have two option
            # 1) add value to current value
            # 2) substract value from current value
            # total number of ways = sum of both ways which sum will equal to target end of the list
            ways = solve(index + 1, remaining + nums[index]) + solve(index + 1, remaining - nums[index])
            memo[(index, remaining)] = ways
            return ways

        return solve(0, 0)