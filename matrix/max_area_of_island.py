from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = []
        for i in range(rows):
            visited.append([0] * cols)

        def flood_fill(x, y, island_number):
            visited[x][y] = 1
            grid[x][y] = island_number
            cell_count[island_number] += 1
            coordinates = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dx, dy in coordinates:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    if grid[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
                        flood_fill(new_x, new_y, island_number)

        island_numebr = 0
        cell_count = {}
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    island_numebr += 1
                    cell_count[island_numebr] = 0
                    flood_fill(i, j, island_numebr)

        return max(cell_count.values()) if len(cell_count) > 0 else 0
