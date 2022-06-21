from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        M = len(matrix)
        N = len(matrix[0])
        mem = {}

        def solve(i, j, v):

            if i < 0 or i >= M or j < 0 or j >= N:
                return 0
            if matrix[i][j] <= v:
                return 0
            if (i, j) in mem:
                return mem[(i, j)]
            subp = max(solve(i, j + 1, matrix[i][j]),
                       solve(i, j - 1, matrix[i][j]),
                       solve(i + 1, j, matrix[i][j]),
                       solve(i - 1, j, matrix[i][j])) + 1
            mem[(i, j)] = subp
            return subp

        ans = 0
        for i in range(M):
            for j in range(N):
                ans = max(ans, solve(i, j, float("-inf")))
        return ans
