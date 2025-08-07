# Medium/palindromic_substring.py

def longestPalindrome(s:str)->str:
    if not s or len(s)<1:
        return ""

    start,end=0,0

    def expandAroundCenter(left:int,right:int)->int:
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return right-left-1  # Length of the palindrome

    for i in range(len(s)):
        len1=expandAroundCenter(i,i)       # Odd length
        len2=expandAroundCenter(i,i+1)   # Even length
        max_len=max(len1,len2)

        if max_len>(end-start):
            start=i-(max_len-1)//2
            end=i+max_len//2

    return s[start:end+1]

if __name__=="__main__":
    print(longestPalindrome("babad"))  # "bab" or "aba"
    print(longestPalindrome("cbbd"))   # "bb"
