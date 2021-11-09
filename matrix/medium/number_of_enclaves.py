from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def flood_fill(x, y):
            grid[x][y] = 2
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for xx, yy in directions:
                newx = x + xx
                newy = y + yy
                if 0 <= newx < rows and 0 <= newy < cols:
                    if grid[newx][newy] == 1:
                        flood_fill(newx, newy)

        for i in range(rows):
            for j in range(cols):
                if 0 < i < rows - 1 and 0 < j < cols - 1:
                    continue
                if grid[i][j] == 1:
                    flood_fill(i, j)
        count = 0
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if grid[i][j] == 1:
                    count += 1
        return count