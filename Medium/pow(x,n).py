class Solution:
    def myPow(self,x:float,n:int)->float:
        if n==0:
            return 1.0
        if n<0:
            x=1/x
            n=-n

        result=1.0
        while n>0:
            if n%2==1:
                result*=x
            x*=x
            n//=2
        return result


if __name__=="__main__":
    # Test cases
    sol=Solution()
    print("Test Case 1: myPow(2.00000, 10) ->", sol.myPow(2.00000, 10))   # Expected 1024.0
    print("Test Case 2: myPow(2.10000, 3) ->", sol.myPow(2.10000, 3))    # Expected 9.261
    print("Test Case 3: myPow(2.00000, -2) ->", sol.myPow(2.00000, -2))  # Expected 0.25
    print("Test Case 4: myPow(1.00000, 2147483647) ->", sol.myPow(1.00000, 2147483647))  # Expected 1.0
    print("Test Case 5: myPow(0.00001, 2147483647) ->", sol.myPow(0.00001, 2147483647))  # Very small number close to 0
