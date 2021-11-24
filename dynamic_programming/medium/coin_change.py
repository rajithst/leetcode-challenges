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


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            dp[i] = float("inf")
            for c in coins:
                if i - c >= 0 and dp[i - c] != float("inf"):
                    dp[i] = min(dp[i], dp[i - c] + 1)

        return -1 if dp[amount] == float("inf") else dp[amount]