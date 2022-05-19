import math


class Solution:
    def numSquares(self, n: int) -> int:
        possible_sqs = [i * i for i in range(1, int(math.sqrt(n)) + 1)]
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        # try to fill all dp boxes from 1 to n
        for val in range(1, n + 1):
            # for each box we have n number of options to check(possible sq values)
            for sq in possible_sqs:
                # current minimum ways = minimum of current value or prev val+1
                dp[val] = min(dp[val], dp[val - sq] + 1)
        return dp[n]

#         possible_sqs = [i*i for i in range(1,int(math.sqrt(n))+1)]
#         memo = {}
#         def solve(rem):
#             if rem == 0:
#                 return 0
#             if rem < 0:
#                 return float("inf")

#             if rem in memo:
#                 return memo[rem]

#             ans = float("inf")
#             for sq in possible_sqs:
#                 ans = min(ans,solve(rem - sq) + 1)
#             memo[rem] = ans
#             return ans
#         return solve(n)



