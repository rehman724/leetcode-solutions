class Solution:
    def minDistance(self,word1:str,word2:str)->int:
        m,n=len(word1),len(word2)

        # DP table
        dp=[[0]*(n+1) for _ in range(m+1)]

        # Base cases
        for i in range(m+1):
            dp[i][0]=i  # word1 to empty string (delete all)
        for j in range(n+1):
            dp[0][j]=j  # empty string to word2 (insert all)

        # Fill DP table
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]  # no operation
                else:
                    dp[i][j]=1+min(
                        dp[i-1][j],  # delete
                        dp[i][j-1],  # insert
                        dp[i-1][j-1]  # replace
                    )

        return dp[m][n]

if __name__=="__main__":
    sol=Solution()
    print(sol.minDistance("horse", "ros"))  # Expected: 3
    print(sol.minDistance("intention", "execution"))  # Expected: 5
    print(sol.minDistance("", "abc"))  # Expected: 3
    print(sol.minDistance("abc", ""))  # Expected: 3
    print(sol.minDistance("abc", "abc"))  # Expected: 0
