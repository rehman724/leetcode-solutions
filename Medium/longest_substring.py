# Medium/longest_substring.py

def lengthOfLongestSubstring(s:str)->int:
    seen=set()
    left=0
    max_length=0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])
        max_length=max(max_length,right-left+1)

    return max_length

# Example usage
if __name__=="__main__":
    s="abcabcbb"
    print("Longest substring without repeating characters:",lengthOfLongestSubstring(s))
