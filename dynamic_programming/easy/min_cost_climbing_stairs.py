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