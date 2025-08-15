class Solution:
    def multiply(self,num1:str,num2:str)->str:
        if num1=="0" or num2=="0":
            return "0"

        m,n=len(num1),len(num2)
        result=[0]*(m+n)

        # Reverse both numbers for easier calculation
        num1,num2=num1[::-1],num2[::-1]

        for i in range(m):
            for j in range(n):
                digit=int(num1[i])*int(num2[j])
                result[i+j]+=digit
                result[i+j+1]+=result[i+j]//10
                result[i+j]%=10

        # Remove leading zeros
        while len(result)>1 and result[-1]==0:
            result.pop()

        return ''.join(map(str,result[::-1]))


# ---------- Test Code ----------
if __name__=="__main__":
    solution=Solution()
    # Example Test Cases
    print(solution.multiply("2", "3"))        # Expected output: "6"
    print(solution.multiply("123", "456"))    # Expected output: "56088"
    print(solution.multiply("0", "1234"))     # Expected output: "0"
