from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        que = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    que.append([i, j])
                    seen.add((i, j))
                    break
            else:
                continue
            break

        while que:
            X, Y = que.popleft()
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for x, y in directions:
                newx = X + x
                newy = Y + y
                if 0 <= newx < rows and 0 <= newy < cols and grid[newx][newy] == 1 and ((newx, newy) not in seen):
                    que.append([newx, newy])
                    seen.add((newx, newy))

        que2 = deque(seen)
        distance = 0
        while que2:
            for _ in range(len(que2)):
                X, Y = que2.popleft()
                directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                for x, y in directions:
                    newx = X + x
                    newy = Y + y
                    if 0 <= newx < rows and 0 <= newy < cols:
                        if grid[newx][newy] == 1 and ((newx, newy) not in seen):
                            return distance
                        elif grid[newx][newy] == 0 and ((newx, newy) not in seen):
                            que2.append([newx, newy])
                            seen.add((newx, newy))
            distance += 1
