class Solution:
    def trap(self,height:list[int])->int:
        if not height:
            return 0

        left,right=0,len(height)-1
        left_max,right_max=height[left],height[right]
        water=0

        while left<right:
            if left_max<right_max:
                left+=1
                left_max=max(left_max,height[left])
                water+=max(0,left_max-height[left])
            else:
                right-=1
                right_max=max(right_max,height[right])
                water+=max(0,right_max-height[right])

        return water


if __name__=="__main__":
    sol=Solution()

    test_cases=[
        ([0,1,0,2,1,0,1,3,2,1,2,1],6),
        ([4,2,0,3,2,5],9),
        ([1,0,1],1),
        ([5,4,1,2],1),
        ([],0)
    ]

    for heights,expected in test_cases:
        result=sol.trap(heights)
        print(f"Input: {heights} | Expected: {expected} | Output: {result} | Pass: {result == expected}")
