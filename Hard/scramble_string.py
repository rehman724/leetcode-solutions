from functools import lru_cache
class Solution:
    def isScramble(self,s1:str,s2:str)->bool:
        # If lengths differ, impossible
        if len(s1)!=len(s2):
            return False
        # Base case: exact match
        if s1==s2:
            return True
        # Early pruning: character frequency mismatch
        if sorted(s1)!=sorted(s2):
            return False

        @lru_cache(None)
        def dfs(a:str,b:str)->bool:
            # If they match directly
            if a==b:
                return True
            # Prune by checking characters
            if sorted(a)!=sorted(b):
                return False

            n=len(a)
            for i in range(1, n):
                # Case 1: No swap
                if dfs(a[:i],b[:i]) and dfs(a[i:],b[i:]):
                    return True
                # Case 2: With swap
                if dfs(a[:i],b[-i:]) and dfs(a[i:],b[:-i]):
                    return True
            return False

        return dfs(s1,s2)


if __name__=="__main__":
    sol=Solution()

    # Example cases
    print(sol.isScramble("great", "rgeat"))  # True
    print(sol.isScramble("abcde", "caebd"))  # False
    print(sol.isScramble("a", "a"))  # True

