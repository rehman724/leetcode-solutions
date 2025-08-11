class Solution:
    def strStr(self,haystack:str,needle:str)->int:
        """
        Finds the first occurrence of needle in haystack.
        If needle is not found, returns -1.

        Approach:
        - Use Python's built-in string find() method (O(n) time complexity).
        - Alternatively, could manually check each starting position.

        Time Complexity: O(n * m) in the worst case, but O(n) with built-in find()
        Space Complexity: O(1)
        """
        return haystack.find(needle)


# Example usage
if __name__=="__main__":
    sol=Solution()
    print(sol.strStr("sadbutsad", "sad"))  # Output: 0
    print(sol.strStr("leetcode", "leeto")) # Output: -1
