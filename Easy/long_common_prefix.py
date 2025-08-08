# Easy/longest_common_prefix.py

def longestCommonPrefix(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):
        char=strs[0][i]
        for s in strs[1:]:
            if i>=len(s) or s[i]!=char:
                return strs[0][:i]
    return strs[0]

if __name__=="__main__":
    print(longestCommonPrefix(["flower","flow","flight"]))  # "fl"
    print(longestCommonPrefix(["dog","racecar","car"]))     # ""
    print(longestCommonPrefix(["inter","internet","internal"]))  # "inter"
