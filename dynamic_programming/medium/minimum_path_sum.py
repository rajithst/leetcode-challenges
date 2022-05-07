from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        M = len(grid)
        N = len(grid[0])
        memo = {}

        def solve(i, j):

            if i >= M:
                return float("inf")
            if j >= N:
                return float("inf")

            if i == M - 1 and j == N - 1:
                return grid[i][j]

            if (i, j) in memo:
                return memo[(i, j)]

            subproblem = min(solve(i, j + 1), solve(i + 1, j)) + grid[i][j]
            memo[(i, j)] = subproblem
            return subproblem

        return solve(0, 0)
