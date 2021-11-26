from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [0] * n
        if len(dp) == 1:
            return nums[0]

        dp[0] = max(0, nums[0])
        dp[1] = max(0, max(nums[0], nums[1]))

        for i in range(2, n):
            inc = nums[i] + dp[i - 2]
            exc = dp[i - 1]
            dp[i] = max(inc, exc)
        return dp[n - 1]


class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def top_down_dp(at):

            if at in memo:
                return memo[at]

            if at == 0:
                return max(0, nums[at])

            if at == 1:
                return max(0, max(nums[0], nums[1]))

            inc = nums[at] + top_down_dp(at - 2)
            exc = top_down_dp(at - 1)
            memo[at] = max(inc, exc)
            return memo[at]

        return top_down_dp(len(nums) - 1)
