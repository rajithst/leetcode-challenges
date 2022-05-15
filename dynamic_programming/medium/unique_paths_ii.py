from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        memo = {}

        def solve(i, j):
            if i >= M or j >= N or obstacleGrid[i][j] == 1:
                return 0

            if i == M - 1 and j == N - 1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]

            subp = solve(i, j + 1) + solve(i + 1, j)
            memo[(i, j)] = subp
            return subp

        return solve(0, 0)
