def jump(nums):
    jumps=0
    current_end=0
    farthest=0

    for i in range(len(nums)-1):
        farthest=max(farthest,i+nums[i])
        if i==current_end:
            jumps+=1
            current_end=farthest

    return jumps

if __name__=="__main__":
    test_cases=[
        ([2,3,1,1,4],2),
        ([2,3,0,1,4],2),
        ([1,2],1),
        ([0],0),
        ([1,1,1,1],3)
    ]

    for nums,expected in test_cases:
        result=jump(nums)
        print(f"nums: {nums} | Expected: {expected} | Got: {result} | Pass: {result == expected}")