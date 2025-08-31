from typing import List
class Solution:
    def subsetsWithDup(self,nums:List[int])->List[List[int]]:

        nums.sort()  # Sort to group duplicates
        res=[]

        def backtrack(start:int,path:List[int])->None:
            res.append(path[:])  # Add current subset
            for i in range(start,len(nums)):
                # Skip duplicates
                if i>start and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()

        backtrack(0, [])
        return res

if __name__=="__main__":
    sol=Solution()

    # Test case 1
    nums1=[1,2,2]
    print("Input:", nums1)
    print("Subsets:", sol.subsetsWithDup(nums1))
    # Expected: [[], [1], [1,2], [1,2,2], [2], [2,2]]

    # Test case 2
    nums2=[0]
    print("\nInput:", nums2)
    print("Subsets:", sol.subsetsWithDup(nums2))
    # Expected: [[], [0]]
