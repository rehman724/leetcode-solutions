class Solution:
    def mySqrt(self,x:int)->int:
        if x<2:
            return x

        left,right=1,x//2
        ans=0
        while left<=right:
            mid=(left+right)//2
            sq=mid*mid
            if sq==x:
                return mid
            if sq<x:
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans


if __name__=="__main__":
    sol=Solution()

    # Example cases
    print(sol.mySqrt(4))   # Expected: 2
    print(sol.mySqrt(8))   # Expected: 2

    # Edge cases
    print(sol.mySqrt(0))   # Expected: 0
    print(sol.mySqrt(1))   # Expected: 1
    print(sol.mySqrt(2))   # Expected: 1
    print(sol.mySqrt(3))   # Expected: 1
    print(sol.mySqrt(15))  # Expected: 3
    print(sol.mySqrt(16))  # Expected: 4
    print(sol.mySqrt(27))  # Expected: 5
    print(sol.mySqrt(100)) # Expected: 10
