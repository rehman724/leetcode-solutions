
from typing import List
class Solution:
    def solveNQueens(self,n:int)->List[List[str]]:
        result=[]
        board=[["."]*n for _ in range(n)]

        cols=set()
        diagonals=set()  # row - col
        anti_diagonals=set()  # row + col

        def backtrack(row:int):
            if row==n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row-col) in diagonals or (row+col) in anti_diagonals:
                    continue

                # Place queen
                board[row][col]="Q"
                cols.add(col)
                diagonals.add(row-col)
                anti_diagonals.add(row+col)

                backtrack(row+1)

                # Remove queen (backtrack)
                board[row][col]="."
                cols.remove(col)
                diagonals.remove(row-col)
                anti_diagonals.remove(row+col)

        backtrack(0)
        return result


if __name__=="__main__":
    sol=Solution()
    print("Test Case 1: n = 4")
    print(sol.solveNQueens(4))
    # Expected:
    # [
    #   [".Q..","...Q","Q...","..Q."],
    #   ["..Q.","Q...","...Q",".Q.."]
    # ]

    print("\nTest Case 2: n = 1")
    print(sol.solveNQueens(1))
    # Expected: [["Q"]]
