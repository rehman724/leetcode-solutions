class Solution:
    def firstMissingPositive(self,nums:list[int])->int:
        n=len(nums)

        # Place each number in its correct position if possible
        for i in range(n):
            while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]

        # Find the first index where the value is not correct
        for i in range(n):
            if nums[i]!=i+1:
                return i+1

        return n+1


if __name__=="__main__":
    sol=Solution()

    test_cases =[
        ([1,2,0],3),
        ([3,4,-1,1],2),
        ([7,8,9,11,12],1),
        ([1,1],2),
        ([2,1],3)
    ]

    for nums,expected in test_cases:
        result=sol.firstMissingPositive(nums.copy())
        print(f"Input: {nums} | Expected: {expected} | Output: {result} | Pass: {result == expected}")
