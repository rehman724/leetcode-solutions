from typing import List

class Solution:
    def maximalRectangle(self,matrix:List[List[str]])->int:
        if not matrix or not matrix[0]:
            return 0

        n=len(matrix[0])
        heights=[0]*(n+1)  # +1 sentinel
        max_area=0

        for row in matrix:
            # Step 1: Build heights histogram for the current row
            for i in range(n):
                heights[i]=heights[i]+1 if row[i]=='1' else 0

            # Step 2: Use Largest Rectangle in Histogram approach
            stack=[]
            for i in range(n+1):
                while stack and heights[stack[-1]]>heights[i]:
                    h=heights[stack.pop()]
                    w=i if not stack else i-stack[-1]-1
                    max_area=max(max_area,h*w)
                stack.append(i)

        return max_area


if __name__=="__main__":
    solver=Solution()

    # Example 1
    matrix1=[
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    print(solver.maximalRectangle(matrix1))  # Expected: 6

    # Example 2
    matrix2=[["0"]]
    print(solver.maximalRectangle(matrix2))  # Expected: 0

