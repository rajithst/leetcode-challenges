from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxs = [set() for _ in range(n)]

        for x in range(n):
            for y in range(n):
                val = board[x][y]
                if val == ".":
                    continue
                # check if already in row values
                if val in rows[x]:
                    return False
                rows[x].add(val)
                # check if already in cols values
                if val in cols[y]:
                    return False
                cols[y].add(val)

                # check its in the box
                box_id = (x // 3) * 3 + y // 3
                if val in boxs[box_id]:
                    return False
                boxs[box_id].add(val)
        return True

