class Solution:
    def climbStairs(self, n: int) -> int:

        def top_down_dp(at):
            if at == 0 or at == 1:
                return 1

            return top_down_dp(at - 1) + top_down_dp(at - 2)

        return top_down_dp(n)

        def bottom_up_dp(n):
            arr = [0] * (n + 1)
            arr[0] = 1
            arr[1] = 1
            for i in range(2, n + 1):
                arr[i] = arr[i - 1] + arr[i - 2]
            return arr[n]

        return bottom_up_dp(n)

        mem = {}

        def top_down_dp_with_memo(at):
            if at == 0 or at == 1:
                return 1
            if at in mem:
                return mem[at]

            mem[at] = top_down_dp_with_memo(at - 1) + top_down_dp_with_memo(at - 2)
            return mem[at]

        return top_down_dp_with_memo(n)
