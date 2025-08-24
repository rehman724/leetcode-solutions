class Solution:
    def climbStairs(self,n:int)->int:
        if n<=2:
            return n

        # DP approach (Fibonacci relation)
        prev1,prev2=1,2
        for _ in range(3,n+1):
            prev1,prev2=prev2,prev1+prev2
        return prev2


if __name__=="__main__":
    sol=Solution()

    # Example cases
    print(sol.climbStairs(2))  # Expected: 2
    print(sol.climbStairs(3))  # Expected: 3

    # Additional cases
    print(sol.climbStairs(1))  # Expected: 1
    print(sol.climbStairs(4))  # Expected: 5
    print(sol.climbStairs(5))  # Expected: 8
    print(sol.climbStairs(6))  # Expected: 13
    print(sol.climbStairs(10))  # Expected: 89
