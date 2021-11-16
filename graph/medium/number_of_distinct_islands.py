from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0] * cols for _ in range(rows)]
        islands = []

        def traverse(x, y, path):
            visited[x][y] = 1
            path.append((x - xo, y - yo))
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for xx, yy in directions:
                newx = x + xx
                newy = y + yy
                if 0 <= newx < rows and 0 <= newy < cols:
                    if visited[newx][newy] == 0 and grid[newx][newy] == 1:
                        traverse(newx, newy, path)

        island_count = 0
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == 0 and grid[i][j] == 1:
                    path = []
                    xo = i
                    yo = j
                    traverse(i, j, path)
                    if path not in islands:
                        island_count += 1
                        islands.append(path)
        return island_count
