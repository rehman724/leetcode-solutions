def nextPermutation(nums: list[int]) -> None:

    # Step 1: Find the first decreasing element from the right
    i=len(nums)-2
    while i>=0 and nums[i]>=nums[i+1]:
        i-=1

    # Step 2: If found, swap with the next greater element from the right
    if i>=0:
        j = len(nums)-1
        while nums[j]<=nums[i]:
            j-=1
        nums[i],nums[j]=nums[j],nums[i]

    # Step 3: Reverse the elements from i+1 to end
    nums[i+1:]=reversed(nums[i+1:])


# Example run
if __name__=="__main__":
    nums=[1, 2, 3]
    nextPermutation(nums)
    print(nums)  # Output: [1, 3, 2]
