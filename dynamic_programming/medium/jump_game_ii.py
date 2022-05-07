from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        memo = {}

        def solve(index, N):
            if index == N - 1:
                return 0

            if index > N - 1:
                return -1
            if index in memo:
                return memo[index]

            min_jumps = float("inf")
            for i in range(1, nums[index] + 1):
                sub_problem_ways = solve(index + i, N)
                if sub_problem_ways != -1:
                    min_jumps = min(min_jumps, sub_problem_ways + 1)

            memo[index] = min_jumps
            return min_jumps

        return solve(0, len(nums))