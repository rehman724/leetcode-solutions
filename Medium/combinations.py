class Solution:
    def combine(self,n:int,k:int):
        res=[]

        def backtrack(start,comb):
            if len(comb)==k:
                res.append(comb[:])
                return

            for i in range(start,n+1):
                comb.append(i)
                backtrack(i+1,comb)
                comb.pop()

        backtrack(1, [])
        return res

if __name__=="__main__":
    sol=Solution()

    # Example 1
    print("Test 1:")
    print("Input: n = 4, k = 2")
    print("Output:", sol.combine(4, 2))  # Expected [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

    # Example 2
    print("\nTest 2:")
    print("Input: n = 1, k = 1")
    print("Output:", sol.combine(1, 1))  # Expected [[1]]

