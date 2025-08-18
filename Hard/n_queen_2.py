class Solution:
    def totalNQueens(self,n:int)->int:
        self.count=0
        cols=set()
        diagonals=set()  # row - col
        anti_diagonals=set()  # row + col
        def backtrack(row:int):
            if row==n:
                self.count+=1
                return

            for col in range(n):
                if col in cols or (row-col) in diagonals or (row+col) in anti_diagonals:
                    continue

                # Place queen
                cols.add(col)
                diagonals.add(row-col)
                anti_diagonals.add(row+col)

                backtrack(row+1)

                # Remove queen (backtrack)
                cols.remove(col)
                diagonals.remove(row-col)
                anti_diagonals.remove(row+col)

        backtrack(0)
        return self.count
