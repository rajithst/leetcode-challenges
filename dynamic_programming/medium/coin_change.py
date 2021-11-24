from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def top_down_dp(at):
            if at == 0:
                return 0

            if at in memo:
                return memo[at]

            min_coins = float("inf")
            for c in coins:
                if at - c >= 0:
                    min_coins = min(min_coins, top_down_dp(at - c) + 1)
            memo[at] = min_coins
            return memo[at]

        res = top_down_dp(amount)
        return -1 if res == float("inf") else res
