from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = {}

        def solve(remaining):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0

            if remaining in memo:
                return memo[remaining]

            ans = 0
            for n in nums:
                ans += solve(remaining - n)
            memo[remaining] = ans
            return ans

        return solve(target)
