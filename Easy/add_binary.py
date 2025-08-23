class Solution:
    def addBinary(self,a:str,b:str)->str:
        """
        Given two binary strings a and b, return their sum as a binary string.
        """
        i,j=len(a)-1,len(b)-1
        carry=0
        result=[]

        while i>=0 or j>=0 or carry:
            total=carry
            if i>=0:
                total+=int(a[i])
                i-=1
            if j>=0:
                total+=int(b[j])
                j-=1
            result.append(str(total%2))
            carry=total//2

        return "".join(reversed(result))


if __name__=="__main__":
    sol=Solution()

    # Test cases
    print("Test Case 1: ", sol.addBinary("11", "1"))      # Expected "100"
    print("Test Case 2: ", sol.addBinary("1010", "1011")) # Expected "10101"
    print("Test Case 3: ", sol.addBinary("0", "0"))       # Expected "0"
    print("Test Case 4: ", sol.addBinary("111", "111"))   # Expected "1110"
    print("Test Case 5: ", sol.addBinary("1", "111111"))  # Expected "1000000"
