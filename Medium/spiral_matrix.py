
from typing import List
class Solution:
    def spiralOrder(self,matrix:List[List[int]])->List[int]:
        result=[]
        if not matrix:
            return result

        top,bottom=0,len(matrix)-1
        left,right=0,len(matrix[0])-1

        while top<=bottom and left<=right:
            # Traverse left → right
            for j in range(left,right+1):
                result.append(matrix[top][j])
            top+=1

            # Traverse top → bottom
            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right-=1

            if top<=bottom:
                # Traverse right → left
                for j in range(right,left-1,-1):
                    result.append(matrix[bottom][j])
                bottom-=1

            if left<=right:
                # Traverse bottom → top
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left+=1

        return result


if __name__=="__main__":
    # Test Cases
    solver=Solution()

    print("Test Case 1:",solver.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    # Expected: [1,2,3,6,9,8,7,4,5]

    print("Test Case 2:", solver.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    # Expected: [1,2,3,4,8,12,11,10,9,5,6,7]

    print("Test Case 3:", solver.spiralOrder([[1]]))
    # Expected: [1]

    print("Test Case 4:", solver.spiralOrder([[1],[2],[3],[4]]))
    # Expected: [1,2,3,4]

    print("Test Case 5:", solver.spiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))
    # Expected: [1,2,3,6,9,12,11,10,7,4,5,8]
