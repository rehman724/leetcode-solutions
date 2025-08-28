from typing import List
class Solution:
    def removeDuplicates(self,nums:List[int])->int:
        if len(nums)<=2:
            return len(nums)

        # write pointer
        k=2
        for i in range(2,len(nums)):
            # keep only if current != nums[k-2]
            if nums[i]!=nums[k-2]:
                nums[k]=nums[i]
                k+=1

        return k


if __name__=="__main__":
    solution=Solution()

    # Test Case 1
    nums1=[1,1,1,2,2,3]
    k1=solution.removeDuplicates(nums1)
    print("Test Case 1:", k1,nums1[:k1])  # Expected: 5, [1,1,2,2,3]

    # Test Case 2
    nums2=[0,0,1,1,1,1,2,3,3]
    k2=solution.removeDuplicates(nums2)
    print("Test Case 2:", k2,nums2[:k2])  # Expected: 7, [0,0,1,1,2,3,3]

