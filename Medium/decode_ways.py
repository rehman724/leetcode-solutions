class Solution:
    def numDecodings(self,s:str)->int:

        if not s or s[0]=="0":
            return 0

        n=len(s)
        dp=[0]*(n+1)

        # Base cases
        dp[0]=1  # Empty string
        dp[1]=1  # First char is valid since it's not '0'

        for i in range(2,n+1):
            one_digit=int(s[i-1])
            two_digits=int(s[i-2:i])

            if one_digit >=1:
                dp[i]+=dp[i-1]
            if 10<=two_digits<=26:
                dp[i]+=dp[i-2]

        return dp[n]


if __name__=="__main__":
    sol=Solution()

    # Example test cases
    assert sol.numDecodings("12")==2  # "AB", "L"
    assert sol.numDecodings("226")==3  # "BZ", "VF", "BBF"

    # Edge cases
    assert sol.numDecodings("0") == 0  # No valid decoding
    assert sol.numDecodings("06") == 0  # Leading zero invalid

    print("All test cases passed!")
