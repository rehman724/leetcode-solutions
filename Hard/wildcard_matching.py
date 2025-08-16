class Solution:
    def isMatch(self,s:str,p:str)->bool:
        m,n=len(s),len(p)
        dp=[[False]*(n+1) for _ in range(m+1)]
        dp[0][0]=True

        # Handle patterns starting with '*'
        for j in range(1,n+1):
            if p[j-1]=='*':
                dp[0][j]=dp[0][j-1]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i-1][j]
                elif p[j-1]=='?' or p[j-1]==s[i-1]:
                    dp[i][j]=dp[i-1][j-1]

        return dp[m][n]


if __name__=="__main__":
    # Test Cases
    solution=Solution()

    test_cases=[
        ("aa","a",False),
        ("aa","*",True),
        ("cb","?a",False),
        ("adceb","*a*b",True),
        ("acdcb","a*c?b",False),
        ("","*",True),
        ("","?",False)
    ]

    for s,p,expected in test_cases:
        result=solution.isMatch(s,p)
        print(f"isMatch({s!r}, {p!r}) = {result} | Expected: {expected} | {'PASS' if result == expected else 'FAIL'}")