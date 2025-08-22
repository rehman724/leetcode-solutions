

from typing import List
class Solution:
    def uniquePathsWithObstacles(self,obstacleGrid:List[List[int]])->int:
        if not obstacleGrid or obstacleGrid[0][0]==1:
            return 0

        m,n=len(obstacleGrid),len(obstacleGrid[0])
        dp=[[0]*n for _ in range(m)]

        # Starting point
        dp[0][0]=1

        # Fill first column
        for i in range(1,m):
            if obstacleGrid[i][0]==0:
                dp[i][0]=dp[i-1][0]

        # Fill first row
        for j in range(1,n):
            if obstacleGrid[0][j]==0:
                dp[0][j]=dp[0][j-1]

        # Fill the rest of dp table
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]

        return dp[m-1][n-1]


if __name__=="__main__":
    sol=Solution()

    # Example test cases
    print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))  # Expected: 2
    print(sol.uniquePathsWithObstacles([[0,1],[0,0]]))  # Expected: 1

    # Additional tests
    print(sol.uniquePathsWithObstacles([[1]]))  # Expected: 0 (start blocked)
    print(sol.uniquePathsWithObstacles([[0]]))  # Expected: 1 (single free cell)
    print(sol.uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))  # Expected: 0 (path blocked)
    print(sol.uniquePathsWithObstacles([[0,0],[0,0]]))  # Expected: 2
