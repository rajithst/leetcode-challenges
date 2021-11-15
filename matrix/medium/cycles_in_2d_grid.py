from typing import List


class Solution:
    def __init__(self):
        self.ans = False

    def containsCycle(self, grid: List[List[str]]) -> bool:

        rows = len(grid)
        cols = len(grid[0])
        visited = [[0] * cols for _ in range(rows)]

        def flood_fill(x, y, px, py, letter):
            visited[x][y] = 1
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for xx, yy in directions:
                newx = x + xx
                newy = y + yy
                if 0 <= newx < rows and 0 <= newy < cols:
                    if visited[newx][newy] == 0 and grid[newx][newy] == letter:
                        flood_fill(newx, newy, x, y, letter)
                    elif visited[newx][newy] == 1 and grid[newx][newy] == letter and (newx, newy) != (px, py):
                        self.ans = True

        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == 0:
                    start = grid[i][j]
                    flood_fill(i, j, -1, -1, start)
                    if self.ans:
                        return self.ans
        return self.ans





