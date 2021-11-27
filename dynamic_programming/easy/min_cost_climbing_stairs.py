from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memo = {}

        def top_down_dp(at):
            if at in memo:
                return memo[at]
            if at <= 1:
                return 0
            memo[at] = min(top_down_dp(at - 1) + cost[at - 1], top_down_dp(at - 2) + cost[at - 2])
            return memo[at]

        return top_down_dp(len(cost))


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])
        return dp[n]