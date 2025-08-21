import math
class Solution:
    def getPermutation(self,n:int,k:int)->str:
        # Create list of numbers from 1 to n
        numbers=[str(i) for i in range(1,n+1)]

        # Adjust k to zero-based index
        k-=1
        result=[]

        for i in range(n,0,-1):
            fact=math.factorial(i-1)
            index=k//fact
            result.append(numbers.pop(index))
            k%=fact

        return "".join(result)


if __name__=="__main__":
    sol=Solution()

    # Example test cases
    print("Test 1:", sol.getPermutation(3, 3))  # Expected "213"
    print("Test 2:", sol.getPermutation(4, 9))  # Expected "2314"
    print("Test 3:", sol.getPermutation(3, 1))  # Expected "123"

    # Edge cases
    print("Test 4:", sol.getPermutation(1, 1))  # Expected "1"
    print("Test 5:", sol.getPermutation(2, 2))  # Expected "21"
