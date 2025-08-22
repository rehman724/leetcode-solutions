from typing import List
class Solution:
    def minPathSum(self,grid:List[List[int]])->int:
        if not grid or not grid[0]:
            return 0

        m,n=len(grid),len(grid[0])

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                elif i==0:
                    grid[i][j]+=grid[i][j-1]
                elif j==0:
                    grid[i][j]+=grid[i-1][j]
                else:
                    grid[i][j]+=min(grid[i-1][j],grid[i][j-1])

        return grid[m-1][n-1]


if __name__=="__main__":
    sol=Solution()

    # Example 1
    grid1=[[1,3,1],[1,5,1],[4,2,1]]
    print("Test Case 1:", sol.minPathSum(grid1))  # Expected: 7

    # Example 2
    grid2=[[1,2,3],[4,5,6]]
    print("Test Case 2:", sol.minPathSum(grid2))  # Expected: 12

    # Single row
    grid3=[[1,2,3,4]]
    print("Test Case 3:", sol.minPathSum(grid3))  # Expected: 10

    # Single column
    grid4=[[1],[2],[3],[4]]
    print("Test Case 4:", sol.minPathSum(grid4))  # Expected: 10

    # Only one element
    grid5=[[5]]
    print("Test Case 5:", sol.minPathSum(grid5))  # Expected: 5
