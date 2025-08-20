
from typing import List
class Solution:
    def insert(self,intervals:List[List[int]],newInterval:List[int])->List[List[int]]:
        result=[]
        i=0
        n=len(intervals)

        # Add all intervals before newInterval
        while i<n and intervals[i][1]<newInterval[0]:
            result.append(intervals[i])
            i+=1

        # Merge overlapping intervals
        while i<n and intervals[i][0]<=newInterval[1]:
            newInterval[0] =min(newInterval[0],intervals[i][0])
            newInterval[1]=max(newInterval[1],intervals[i][1])
            i+=1
        result.append(newInterval)

        # Add remaining intervals
        while i<n:
            result.append(intervals[i])
            i+=1

        return result


if __name__=="__main__":
    solution=Solution()

    # Test Case 1
    intervals=[[1,3],[6,9]]
    newInterval=[2,5]
    print("Input:", intervals, "New Interval:", newInterval)
    print("Output:", solution.insert(intervals, newInterval))  # [[1,5],[6,9]]

    # Test Case 2
    intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval=[4,8]
    print("\nInput:", intervals, "New Interval:", newInterval)
    print("Output:", solution.insert(intervals, newInterval))  # [[1,2],[3,10],[12,16]]

    # Test Case 3 (empty intervals)
    intervals=[]
    newInterval=[5, 7]
    print("\nInput:", intervals, "New Interval:", newInterval)
    print("Output:", solution.insert(intervals, newInterval))  # [[5,7]]


