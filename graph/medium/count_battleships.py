from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        rows = len(board)
        cols = len(board[0])
        visited = [[0] * cols for _ in range(rows)]

        def visit_ship(x, y):
            visited[x][y] = 1
            directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            for xx, yy in directions:
                newx = x + xx
                newy = y + yy
                if 0 <= newx < rows and 0 <= newy < cols and visited[newx][newy] == 0 and board[newx][newy] == "X":
                    visit_ship(newx, newy)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] == 0 and board[i][j] == "X":
                    visit_ship(i, j)
                    count += 1
        return count
