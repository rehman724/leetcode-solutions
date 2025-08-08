# Medium/3sum.py

def threeSum(nums):
    res=[]
    nums.sort()
    n=len(nums)

    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:  # Skip duplicate elements
            continue

        left,right=i+1,n-1

        while left<right:
            total=nums[i]+nums[left]+nums[right]
            if total==0:
                res.append([nums[i],nums[left],nums[right]])

                # Skip duplicates
                while left<right and nums[left]==nums[left+1]:
                    left+=1
                while left<right and nums[right]==nums[right-1]:
                    right-=1

                left+=1
                right-=1

            elif total<0:
                left+=1
            else:
                right-=1
    return res

if __name__=="__main__":
    print(threeSum([-1,0,1,2,-1,-4]))  # [[-1, -1, 2], [-1, 0, 1]]
    print(threeSum([0,0,0]))  # [[0, 0, 0]]
