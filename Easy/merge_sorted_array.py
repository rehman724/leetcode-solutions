from typing import List
class Solution:
    def merge(self,nums1:List[int],m:int,nums2:List[int],n:int)->None:

        i,j,k=m-1,n-1,m+n-1

        while i>=0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1

        # Copy any remaining nums2 elements
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1


if __name__=="__main__":
    sol=Solution()

    # Test Case 1
    nums1=[1,2,3,0,0,0]
    nums2=[2,5,6]
    sol.merge(nums1, 3, nums2, 3)
    print(nums1)  # Expected: [1,2,2,3,5,6]

    # Test Case 2
    nums1=[1]
    nums2=[]
    sol.merge(nums1, 1, nums2, 0)
    print(nums1)  # Expected: [1]

