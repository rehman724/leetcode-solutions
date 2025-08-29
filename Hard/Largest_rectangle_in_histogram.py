from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack=[]  # stores indices of bars
        max_area=0
        heights.append(0)  # sentinel to flush out stack at end

        for i,h in enumerate(heights):
            while stack and heights[stack[-1]]>h:
                height=heights[stack.pop()]
                width=i if not stack else i-stack[-1]-1
                max_area=max(max_area,height*width)
            stack.append(i)

        heights.pop()  # restore input
        return max_area


if __name__=="__main__":
    solution=Solution()

    # Test Case 1
    heights=[2,1,5,6,2,3]
    print("Input:", heights, "=> Output:", solution.largestRectangleArea(heights))  # 10

    # Test Case 2
    heights = [2, 4]
    print("Input:", heights, "=> Output:", solution.largestRectangleArea(heights))  # 4

