def search(nums:list[int],target:int)->int:
    left,right=0,len(nums)-1

    while left<=right:
        mid=(left+right)//2

        if nums[mid]==target:
            return mid

        # Left side is sorted
        if nums[left]<=nums[mid]:
            if nums[left]<=target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        # Right side is sorted
        else:
            if nums[mid]<target<=nums[right]:
                left=mid+1
            else:
                right=mid-1

    return -1


if __name__=="__main__":
    test_cases = [
        ([4,5,6,7,0,1,2],0,4),
        ([4,5,6,7,0,1,2],3,-1),
        ([1],0,-1),
        ([1,3],3,1),
        ([6,7,8,1,2,3,4,5],2,4)
    ]

    for nums,target,expected in test_cases:
        result=search(nums,target)
        print(f"Input: {nums}, Target: {target} | Expected: {expected} | Got: {result}")