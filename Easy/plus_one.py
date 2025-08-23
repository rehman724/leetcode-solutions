from typing import List

class Solution:
    def plusOne(self,digits:List[int])->List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+digits

if __name__=="__main__":
    sol=Solution()

    # Basic cases
    assert sol.plusOne([1,2,3])==[1,2,4]   # 123 + 1 = 124
    assert sol.plusOne([4,3,2,1])==[4,3,2,2]  # 4321 + 1 = 4322
    assert sol.plusOne([9])==[1,0]   # 9 + 1 = 10
    assert sol.plusOne([9,9,9])==[1,0,0,0]   # 999 + 1 = 1000
    assert sol.plusOne([0])==[1]   # 0 + 1 = 1

    print("All test cases passed!")
