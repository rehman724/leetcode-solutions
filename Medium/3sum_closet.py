# Medium/3sum_closest.py

def threeSumClosest(nums, target):
    nums.sort()
    closest=float('inf')
    result=0

    for i in range(len(nums)-2):
        left=i+1
        right=len(nums)-1

        while left<right:
            total=nums[i]+nums[left]+nums[right]
            diff=abs(target-total)

            if diff<closest:
                closest=diff
                result=total

            if total<target:
                left+=1
            elif total>target:
                right-=1
            else:
                return total  # exact match
    return result

if __name__=="__main__":
    print(threeSumClosest([-1,2,1,-4], 1))  # Output: 2
    print(threeSumClosest([0,0,0], 1))       # Output: 0
