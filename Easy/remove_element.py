


class Solution:
    def removeElement(self,nums,val):
        """
        Removes all instances of val in nums in-place.

        Args:
            nums (List[int]): The list of integers.
            val (int): The value to remove.

        Returns:
            int: The number of elements not equal to val.
        """
        k=0  # position to insert next non-val element

        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1

        return k


if __name__=="__main__":
    nums=[3,2,2,3]
    val=3
    solution=Solution()
    new_length=solution.removeElement(nums,val)
    print("New Length:",new_length)
    print("Modified nums:",nums[:new_length])  # Valid portion only
