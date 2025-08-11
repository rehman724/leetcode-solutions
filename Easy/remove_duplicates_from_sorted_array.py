
from typing import List

class Solution:
    def removeDuplicates(self,nums:List[int])->int:
        """
        Removes duplicates from sorted array in-place.

        Args:
            nums (List[int]): Sorted list of integers.

        Returns:
            int: Number of unique elements.
        """
        if not nums:
            return 0

        # Pointer for the position of the last unique element
        k=1

        for i in range(1,len(nums)):
            if nums[i]!=nums[i - 1]:
                nums[k]=nums[i]
                k+=1

        return k


if __name__=="__main__":
    # Example usage
    sol=Solution()

    nums=[0,0,1,1,1,2,2,3,3,4]
    k=sol.removeDuplicates(nums)

    print("Number of unique elements:",k)
    print("Array after removing duplicates:",nums[:k])
