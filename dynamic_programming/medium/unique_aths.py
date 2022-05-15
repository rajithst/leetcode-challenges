class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        M = m
        N = n
        memo = {}

        def solve(i, j):
            if i >= M or j >= N:
                return 0

            if i == M - 1 and j == N - 1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]

            subp = solve(i, j + 1) + solve(i + 1, j)
            memo[(i, j)] = subp
            return subp

        return solve(0, 0)
