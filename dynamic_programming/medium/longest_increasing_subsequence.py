from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [1] * n

        max_len = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    max_len = max(max_len, dp[i])
        return max_len


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = {}

        def top_down_dp(at):

            if at in memo:
                return memo[at]

            if at == 0:
                memo[at] = 1
                return memo[at]

            lis = 1
            for i in range(at):
                if nums[at] > nums[i]:
                    lis = max(lis, top_down_dp(i) + 1)
            memo[at] = lis
            return memo[at]

        m = 1
        for i in range(len(nums)):
            m = max(m, top_down_dp(i))
        return m
