class Solution:
    def uniquePaths(self,m:int,n:int)->int:
        # Dynamic Programming approach
        dp=[[1]*n for _ in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]

        return dp[m-1][n-1]


if __name__=="__main__":
    sol=Solution()

    # Example test cases
    print(sol.uniquePaths(3, 7))   # Expected: 28
    print(sol.uniquePaths(3, 2))   # Expected: 3

    # Additional tests
    print(sol.uniquePaths(7, 3))   # Expected: 28
    print(sol.uniquePaths(3, 3))   # Expected: 6
    print(sol.uniquePaths(1, 1))   # Expected: 1
    print(sol.uniquePaths(10, 10)) # Expected: 48620
