from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])

        def flood_fill(X, Y):
            board[X][Y] = "T"
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for x, y in directions:
                new_x = X + x
                new_y = Y + y
                if 0 < new_x < rows and 0 < new_y < cols:
                    if board[new_x][new_y] == "O":
                        flood_fill(new_x, new_y)

        for i in range(rows):
            for j in range(cols):
                if 0 < i < rows - 1 and 0 < j < cols - 1:
                    continue
                if board[i][j] == "O":
                    flood_fill(i, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
