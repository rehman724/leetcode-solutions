
from typing import List
class Solution:
    def generateMatrix(self,n:int)->List[List[int]]:
        # Initialize n x n matrix with zeros
        matrix=[[0]*n for _ in range(n)]

        # Directions: right, down, left, up
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        dir_idx=0  # start with moving right

        row,col=0,0
        for num in range(1,n*n+1):
            matrix[row][col]=num

            # Calculate next position
            next_row=row+directions[dir_idx][0]
            next_col=col+directions[dir_idx][1]

            # If out of bounds or already filled → change direction
            if (next_row<0 or next_row>=n or
                    next_col<0 or next_col>=n or
                    matrix[next_row][next_col]!=0):
                dir_idx=(dir_idx+1)%4
                next_row=row+directions[dir_idx][0]
                next_col=col+directions[dir_idx][1]

            row,col=next_row,next_col

        return matrix


if __name__=="__main__":
    # Test cases
    solution=Solution()

    print("Test Case 1: n = 3")
    print(solution.generateMatrix(3))
    # Expected: [[1,2,3],[8,9,4],[7,6,5]]

    print("\nTest Case 2: n = 1")
    print(solution.generateMatrix(1))
    # Expected: [[1]]

