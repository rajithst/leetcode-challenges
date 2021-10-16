from _ast import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def flood_fill(x, y):
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            grid[x][y] = 0
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    if grid[new_x][new_y] == "1":
                        flood_fill(new_x, new_y)

        island_count = 0
        for i in range(rows):
            for j in range(cols):
                cell = grid[i][j]
                if cell == "1":
                    island_count += 1
                    flood_fill(i, j)
        return island_count