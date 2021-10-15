from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        distance = []
        for i in range(rows):
            distance.append([float("inf")] * cols)

        fresh_oranges = 0
        que = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    que.append((i, j))
                    distance[i][j] = 0
                elif grid[i][j] == 0:
                    distance[i][j] = -2
                else:
                    fresh_oranges += 1

        while que:
            cn = que.popleft()
            x, y = cn
            coordinates = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dx, dy in coordinates:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    if grid[new_x][new_y] == 1 and distance[new_x][new_y] == float("inf"):
                        que.append((new_x, new_y))
                        distance[new_x][new_y] = distance[x][y] + 1
                        fresh_oranges -= 1

        minutes = 0
        for i in range(rows):
            for j in range(cols):
                minutes = max(minutes, distance[i][j])
        if minutes == float("inf"):
            minutes = -1
        return minutes