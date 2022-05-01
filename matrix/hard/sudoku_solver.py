class SudokuRes:
    def __init__(self):
        self.result = None


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def safe_to_place(board, x, y, num, N):

            # check if row or column has target num value
            for k in range(N):
                if board[k][y] == str(num) or board[x][k] == str(num):
                    return False

            # check if subgrid has target value
            subgrid_x = (x // 3) * 3  # start x of subgrid
            subgrid_y = (y // 3) * 3  # start y of subgrid
            for xx in range(subgrid_x, subgrid_x + 3):
                for yy in range(subgrid_y, subgrid_y + 3):
                    if board[xx][yy] == str(num):
                        return False
            return True

        def solve(board, current_row, current_col, N, info):

            # base case,if all rows has finished,it is a valid sudoku solution
            if current_row == N:
                info.result = board
                return True

            # if column is finished,go to next row and solve subproblem
            if current_col == N:
                return solve(board, current_row + 1, 0, N, info)
            # if current cell is already filled,solved subproblem starting from next cell
            if board[current_row][current_col] != ".":
                return solve(board, current_row, current_col + 1, N, info)
            # if current cell is empty,try to put number from 1 to 9 and try to solve subproblem                 #
            # from next cell
            for number in range(1, N + 1):
                # check if number is safe to place
                if safe_to_place(board, current_row, current_col, number, N):
                    # if valid number,update board and try to solve subproblem from next cell
                    board[current_row][current_col] = str(number)
                    # if subproblem can be solved return True to previous call
                    # if everything is fined,this will propegate to main and finish the recursion
                    is_sub_problem_solved = solve(board, current_row, current_col + 1, N, info)
                    if is_sub_problem_solved:
                        return True
                    # otherwise,iterate through all 9 numbers and try to solve subproblem
            # if any of 9 numbers did not work,something wrong with previous cells
            # backtrack and reset current cell to empty and return Flase to previous call
            board[current_row][current_col] = "."
            return False

        N = 9
        info = SudokuRes()
        solve(board, 0, 0, N, info)
        return info.result
