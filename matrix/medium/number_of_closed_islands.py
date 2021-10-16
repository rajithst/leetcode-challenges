from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def flood_fill(x, y):

            if grid[x][y] or grid[x][y] == -1:
                return True

            if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
                return False
            grid[x][y] = -1

            up = flood_fill(x - 1, y)
            right = flood_fill(x, y + 1)
            down = flood_fill(x + 1, y)
            left = flood_fill(x, y - 1)
            return up and right and down and left

        islands = 0
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if grid[i][j] == 0:
                    if flood_fill(i, j):
                        islands += 1
        return islands
