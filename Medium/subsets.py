from typing import List
class Solution:
    def subsets(self,nums:List[int])->List[List[int]]:
        res=[]

        def backtrack(start,path):
            res.append(path[:])  # add current subset
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()

        backtrack(0, [])
        return res


if __name__=="__main__":
    sol=Solution()

    # Test 1
    nums=[1,2,3]
    print("Input:", nums)
    print("Subsets:", sol.subsets(nums))
    # Expected: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

    # Test 2
    nums = [0]
    print("\nInput:", nums)
    print("Subsets:", sol.subsets(nums))
    # Expected: [[], [0]]

