from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        M = len(grid)
        N = len(grid[0])
        mem = {}

        def solve(i, j, v):

            if i < 0 or i >= M or j < 0 or j >= N:
                return 0
            if grid[i][j] <= v:
                return 0
            if (i, j) in mem:
                return mem[(i, j)]
            subp = (solve(i, j + 1, grid[i][j]) +
                    solve(i, j - 1, grid[i][j]) +
                    solve(i + 1, j, grid[i][j]) +
                    solve(i - 1, j, grid[i][j])) + 1
            mem[(i, j)] = subp
            return subp

        ans = 0
        for i in range(M):
            for j in range(N):
                ans += solve(i, j, float("-inf"))
        return ans % 1000000007
        x

