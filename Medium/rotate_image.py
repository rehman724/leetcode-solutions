from typing import List


class Solution:
    def rotate(self,matrix:List[List[int]])->None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()

if __name__=="__main__":
    sol=Solution()

    # Test 1
    matrix1=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    sol.rotate(matrix1)
    print("Rotated Matrix 1:", matrix1)
    # Expected: [[7,4,1],[8,5,2],[9,6,3]]

    # Test 2
    matrix2=[
        [5,1,9,11],
        [2,4,8,10],
        [13,3,6,7],
        [15,14,12,16]
    ]
    sol.rotate(matrix2)
    print("Rotated Matrix 2:", matrix2)
    # Expected: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    # Test 3
    matrix3=[[1]]
    sol.rotate(matrix3)
    print("Rotated Matrix 3:", matrix3)
    # Expected: [[1]]
