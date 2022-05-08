from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        N = len(triangle)
        memo = {}

        def solve(row, index):
            if row == N - 1:
                return triangle[row][index]
            if (row, index) in memo:
                return memo[(row, index)]

            sub_problem = min(solve(row + 1, index), solve(row + 1, index + 1)) + triangle[row][index]
            memo[(row, index)] = sub_problem
            return sub_problem

        return solve(0, 0)
