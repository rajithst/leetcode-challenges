class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def top_down_dp(at):
            if at == 0:
                return 0
            if at == 1:
                return 1
            if at == 2:
                return 1
            if at in memo:
                return memo[at]
            memo[at] = top_down_dp(at - 1) + top_down_dp(at - 2) + top_down_dp(at - 3)
            return memo[at]

        return top_down_dp(n)