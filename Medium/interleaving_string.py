class Solution:
    def isInterleave(self,s1:str,s2:str,s3:str)->bool:
        m,n=len(s1),len(s2)

        # Length mismatch check
        if m+n!=len(s3):
            return False

        # DP table (m+1) x (n+1)
        dp=[[False]*(n+1) for _ in range(m+1)]
        dp[0][0]=True

        # Fill first row
        for j in range(1,n+1):
            dp[0][j]=dp[0][j-1] and s2[j-1]==s3[j-1]

        # Fill first column
        for i in range(1,m+1):
            dp[i][0]=dp[i-1][0] and s1[i-1]==s3[i-1]

        # Fill rest of table
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j]=(dp[i-1][j] and s1[i-1]==s3[i+j-1]) or \
                           (dp[i][j-1] and s2[j-1]==s3[i+j-1])

        return dp[m][n]


# ----------------- TESTING -----------------
if __name__=="__main__":
    sol=Solution()

    test_cases=[
        ("aabcc","dbbca","aadbbcbcac",True),
        ("aabcc","dbbca","aadbbbaccc",False),
        ("", "", "", True),
        ("","abc","abc",True),
        ("abc","","abc",True),
        ("abc","def","adbcef",True),
        ("abc","def","abdecf",True),
        ("abc","def","abdfec",False),
    ]

    for i,(s1,s2,s3,expected) in enumerate(test_cases,1):
        result=sol.isInterleave(s1,s2,s3)
        print(f"Test Case {i}: isInterleave({s1}, {s2}, {s3}) = {result} "
              f"{' PASS' if result == expected else ' FAIL'}")
