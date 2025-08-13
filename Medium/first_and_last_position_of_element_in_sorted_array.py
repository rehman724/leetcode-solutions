from typing import List

class Solution:
    def searchRange(self,nums:List[int],target:int)->List[int]:
        def find_bound(is_first):
            left,right=0,len(nums)-1
            bound=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    bound=mid
                    if is_first:
                        right=mid-1  # Search on the left side
                    else:
                        left=mid+1   # Search on the right side
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return bound

        first_pos=find_bound(True)
        last_pos=find_bound(False)
        return [first_pos,last_pos]
