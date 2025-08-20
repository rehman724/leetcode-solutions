
from typing import List
class Solution:
    def merge(self,intervals:List[List[int]])->List[List[int]]:
        intervals.sort(key=lambda x:x[0])  # Sort by start time
        merged=[]

        for interval in intervals:
            if not merged or merged[-1][1]<interval[0]:
                merged.append(interval)
            else:
                merged[-1][1]=max(merged[-1][1],interval[1])  # Merge overlapping intervals

        return merged


if __name__=="__main__":
    # Test cases
    solution=Solution()

    test_cases=[
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]],[[1,5]]),
        ([[1,4],[0,4]],[[0,4]]),
        ([[1,4],[0,2],[3,5]],[[0,5]]),
        ([[1,10],[2,6],[8,10]],[[1,10]])
    ]

    for intervals, expected in test_cases:
        result=solution.merge(intervals)
        print(f"Input: {intervals} | Expected: {expected} | Got: {result}")
        assert result == expected, f"Test failed for input: {intervals}"

    print("All test cases passed!")
