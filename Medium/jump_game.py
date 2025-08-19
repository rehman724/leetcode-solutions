
from typing import List
class Solution:
    def canJump(self,nums:List[int])->bool:
        max_reach=0
        for i,jump in enumerate(nums):
            if i>max_reach:
                return False
            max_reach=max(max_reach,i+jump)
        return True


if __name__=="__main__":
    # Test cases
    solution=Solution()

    test_cases=[
        ([2,3,1,1,4], True),   # Can reach the end
        ([3,2,1,0,4], False),  # Stuck at index 3
        ([0],True),               # Already at the last index
        ([2,0,0], True),         # Can jump directly
        ([1,1,0,1], False)      # Blocked before the last index
    ]

    for nums, expected in test_cases:
        result=solution.canJump(nums)
        print(f"Input: {nums} | Expected: {expected} | Got: {result}")
        assert result == expected, f"Test failed for input: {nums}"

    print("All test cases passed!")
