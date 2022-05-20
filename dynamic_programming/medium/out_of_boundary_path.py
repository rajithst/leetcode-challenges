class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        memo = {}

        def solve(i, j, steps):

            if i >= m or i < 0 or j >= n or j < 0:
                return int(steps <= maxMove)

            if steps > maxMove:
                return 0

            if (i, j, steps) in memo:
                return memo[(i, j, steps)]
            ways = 0
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for x, y in directions:
                new_i = i + x
                new_j = j + y
                ways += solve(new_i, new_j, steps + 1)
            memo[(i, j, steps)] = ways
            return ways

        return solve(startRow, startColumn, 0) % (10 ** 9 + 7)
