from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        border_x_min, border_x_max = 0, len(grid) - 1
        border_y_min, border_y_max = 0, len(grid) - 1

        def get_coordinates(Y, X):
            directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
            neis = []
            for y, x in directions:
                new_y = Y + y
                new_x = X + x

                within_x_borders = (border_x_min <= new_x <= border_x_max)
                within_y_borders = (border_y_min <= new_y <= border_y_max)
                if within_x_borders and within_y_borders:
                    if grid[new_y][new_x] == 0:
                        neis.append((new_y, new_x))
            return neis

        start_y = 0
        start_x = 0
        if grid[start_y][start_x] == 1:
            return -1
        target = (len(grid) - 1, len(grid) - 1)
        que = deque()
        que.append((start_y, start_x))
        grid[start_y][start_x] = 1
        while que:
            current_y, current_x = que.popleft()
            distance = grid[current_y][current_x]
            if target == (current_y, current_x):
                return distance
            cell_neighbrs = get_coordinates(current_y, current_x)
            for nei in cell_neighbrs:
                grid[nei[0]][nei[1]] = distance + 1
                que.append(nei)
        return -1