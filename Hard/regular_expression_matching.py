# Hard/regular_expression_matching.py

def isMatch(s:str,p:str)->bool:
    memo={}

    def dp(i,j):
        if (i,j) in memo:
            return memo[(i,j)]

        if j==len(p):
            return i==len(s)

        first_match=i<len(s) and (p[j]==s[i] or p[j]=='.')

        if j+1 < len(p) and p[j+1]=='*':
            memo[(i,j)] = (dp(i,j+2) or (first_match and dp(i+1,j)))
        else:
            memo[(i,j)]=first_match and dp(i+1,j+1)

        return memo[(i,j)]

    return dp(0, 0)


if __name__=="__main__":
    print(isMatch("aa", "a"))             # False
    print(isMatch("aa", "a*"))            # True
    print(isMatch("ab", ".*"))            # True
    print(isMatch("mississippi", "mis*is*p*."))  # False
