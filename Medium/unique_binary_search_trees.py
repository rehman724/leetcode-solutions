class Solution:
    def numTrees(self,n:int)->int:
        # DP array
        dp=[0]*(n+1)
        dp[0],dp[1]=1,1

        # Fill DP table
        for nodes in range(2,n+1):
            for root in range(1,nodes+1):
                dp[nodes]+=dp[root-1]*dp[nodes-root]

        return dp[n]


if __name__=="__main__":
    solution=Solution()

    # Expected output: 5
    print(solution.numTrees(3))

    # Expected output: 1
    print(solution.numTrees(1))

    # Expected output: 14
    print(solution.numTrees(4))
