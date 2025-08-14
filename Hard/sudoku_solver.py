from typing import List

class Solution:


    def solveSudoku(self,board:List[List[str]])->None:
        """
        Solves the Sudoku board in-place.
        :param board: List[List[str]] - 9x9 Sudoku grid
        """
        def is_valid(row:int,col:int,char:str)->bool:
            # Check row
            for c in range(9):
                if board[row][c]==char:
                    return False
            # Check column
            for r in range(9):
                if board[r][col]==char:
                    return False
            # Check 3x3 subgrid
            start_row,start_col=(row//3)*3,(col//3)*3
            for r in range(start_row,start_row+3):
                for c in range(start_col,start_col+3):
                    if board[r][c]==char:
                        return False
            return True

        def backtrack()->bool:
            for r in range(9):
                for c in range(9):
                    if board[r][c]=='.':
                        for num in map(str,range(1,10)):
                            if is_valid(r,c,num):
                                board[r][c]=num
                                if backtrack():
                                    return True
                                board[r][c]='.'
                        return False
            return True

        backtrack()

if __name__=="__main__":
    sudoku_board=[
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    print("Original Sudoku:")
    for row in sudoku_board:
        print(row)

    Solution().solveSudoku(sudoku_board)

    print("\nSolved Sudoku:")
    for row in sudoku_board:
        print(row)
