from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = []
        for i in range(rows):
            visited.append([0] * cols)

        def perm(x, y):

            if x < 0 or x > rows - 1 or y < 0 or y > cols - 1 or grid[x][y] == 0:
                return 1

            if visited[x][y]:
                return 0

            visited[x][y] = 1

            return perm(x - 1, y) + perm(x + 1, y) + perm(x, y + 1) + perm(x, y - 1)

        X, Y = 0, 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    X, Y = i, j
                    break
        res = perm(X, Y)
        return res
