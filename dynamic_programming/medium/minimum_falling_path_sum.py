from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        N = len(matrix)
        memo = {}

        def solve(row, col):

            if col < 0 or col >= N:
                return float("inf")
            if row == N - 1:
                return matrix[row][col]
            if (row, col) in memo:
                return memo[(row, col)]

            sub_problem = min(solve(row + 1, col - 1), solve(row + 1, col), solve(row + 1, col + 1)) + matrix[row][col]
            memo[(row, col)] = sub_problem
            return sub_problem

        res = float("inf")
        for i in range(N):
            res = min(res, solve(0, i))
        return res


