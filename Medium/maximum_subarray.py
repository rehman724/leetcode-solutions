
from typing import List
class Solution:
    def maxSubArray(self,nums:List[int])->int:
        current_sum=nums[0]
        max_sum=nums[0]

        for i in range(1,len(nums)):
            current_sum=max(nums[i],current_sum+nums[i])
            max_sum=max(max_sum,current_sum)

        return max_sum


if __name__=="__main__":
    # Test Cases
    solver=Solution()

    print("Test Case 1:", solver.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Expected: 6
    print("Test Case 2:", solver.maxSubArray([1]))  # Expected: 1
    print("Test Case 3:", solver.maxSubArray([5,4,-1,7,8]))  # Expected: 23
    print("Test Case 4:", solver.maxSubArray([-1,-2,-3,-4]))  # Expected: -1
    print("Test Case 5:", solver.maxSubArray([0,-3,5,-2,9,-8,-6]))  # Expected: 12
