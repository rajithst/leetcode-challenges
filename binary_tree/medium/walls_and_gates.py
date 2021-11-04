from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        rows = len(rooms)
        cols = len(rooms[0])
        que = deque()
        for m in range(rows):
            for n in range(cols):
                if rooms[m][n] == 0:
                    que.append([m, n])

        while que:
            X, Y = que.popleft()
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for x, y in directions:
                newX = X + x
                newY = Y + y
                if 0 <= newX < rows and 0 <= newY < cols:
                    if rooms[newX][newY] == 2147483647:
                        rooms[newX][newY] = rooms[X][Y] + 1
                        que.append([newX, newY])