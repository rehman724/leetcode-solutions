from typing import List
class Solution:
    def grayCode(self,n:int)->List[int]:

        return [i^(i>>1) for i in range(1<<n)]


if __name__=="__main__":
    sol=Solution()

    # Example 1
    n=2
    print("Input:", n)
    print("Gray Code:", sol.grayCode(n))
    # Expected: [0,1,3,2] or another valid sequence

    # Example 2
    n=1
    print("\nInput:", n)
    print("Gray Code:", sol.grayCode(n))
    # Expected: [0,1]

