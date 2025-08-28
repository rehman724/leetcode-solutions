from typing import List
class Solution:
    def search(self,nums:List[int],target:int)->bool:
        left,right=0,len(nums)-1

        while left<=right:
            mid=(left+right)//2

            if nums[mid]==target:
                return True

            # Handle duplicates
            if nums[left]==nums[mid]==nums[right]:
                left+=1
                right-=1
            elif nums[left]<=nums[mid]:  # Left half is sorted
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:  # Right half is sorted
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1

        return False


# ------------------------------
# ✅ Test Cases
# ------------------------------
if __name__=="__main__":
    solution=Solution()

    # Example 1
    nums=[2,5,6,0,0,1,2]
    target=0
    print("Input:", nums, "Target:", target, "Output:", solution.search(nums,target))  # True

    # Example 2
    nums=[2,5,6,0,0,1,2]
    target=3
    print("Input:", nums, "Target:", target, "Output:", solution.search(nums,target))  # False

