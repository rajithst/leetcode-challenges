from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        rows = len(land)
        cols = len(land[0])
        visited = [[0] * cols for _ in range(rows)]

        def flood_fill(X, Y, path):
            visited[X][Y] = 1
            x1, y1, x2, y2 = path
            path = [min(X, x1), min(Y, y1), max(X, x2), max(Y, y2)]
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for x, y in directions:
                nx = x + X
                ny = y + Y
                if 0 <= nx < rows and 0 <= ny < cols:
                    if land[nx][ny] == 1 and visited[nx][ny] == 0:
                        return flood_fill(nx, ny, path)
            return path

        paths = []
        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1 and visited[i][j] == 0:
                    res = flood_fill(i, j, [i, j, i, j])
                    paths.append(res)
        return paths
