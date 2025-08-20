class Solution:
    def lengthOfLastWord(self,s:str)->int:
        # Strip trailing spaces and split into words
        words=s.strip().split()
        # Return the length of the last word
        return len(words[-1]) if words else 0


if __name__=="__main__":
    sol=Solution()

    # Test case 1
    s1="Hello World"
    print(f"Input: '{s1}' | Output: {sol.lengthOfLastWord(s1)}")  # Expected: 5

    # Test case 2
    s2="   fly me   to   the moon  "
    print(f"Input: '{s2}' | Output: {sol.lengthOfLastWord(s2)}")  # Expected: 4

