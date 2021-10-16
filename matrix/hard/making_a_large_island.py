from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = []
        for i in range(rows):
            visited.append([0] * cols)

        island_colors = 0
        island_sizes = {}
        island_sizes[island_colors] = 0

        def flood_fill(x, y, color):
            grid[x][y] = color
            visited[x][y] = 1
            island_sizes[color] += 1
            coordinates = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dx, dy in coordinates:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    if grid[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
                        flood_fill(new_x, new_y, color)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    island_colors += 1
                    island_sizes[island_colors] = 0
                    flood_fill(i, j, island_colors)

        max_island_size = max(island_sizes.values())

        for ii in range(rows):
            for jj in range(cols):
                if grid[ii][jj] == 0:
                    coordinates = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                    nei_set = set()
                    for dx, dy in coordinates:
                        new_i = ii + dx
                        new_j = jj + dy
                        if 0 <= new_i < rows and 0 <= new_j < cols:
                            nei_set.add(grid[new_i][new_j])

                    this_island_size = 1
                    for color in nei_set:
                        this_island_size += island_sizes[color]

                    max_island_size = max(max_island_size, this_island_size)
        return max_island_size