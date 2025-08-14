"""
LeetCode Problem: Combination Sum II
Link: https://leetcode.com/problems/combination-sum-ii/

Description:
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.

Constraints:
- All numbers (including target) are positive integers.
- The solution set must not contain duplicate combinations.
"""

from typing import List

class Solution:
    def combinationSum2(self,candidates:List[int],target:int)->List[List[int]]:
        candidates.sort()
        result=[]

        def backtrack(remaining,start,path):
            if remaining==0:
                result.append(path[:])
                return
            elif remaining<0:
                return

            prev=-1
            for i in range(start, len(candidates)):
                if candidates[i]==prev:
                    continue
                path.append(candidates[i])
                backtrack(remaining-candidates[i],i+1,path)
                path.pop()
                prev=candidates[i]

        backtrack(target, 0, [])
        return result


# -------------------- TEST CODE --------------------
if __name__=="__main__":
    sol=Solution()

    # Test case 1
    candidates=[10,1,2,7,6,1,5]
    target=8
    print("Test Case 1:")
    print("Candidates:", candidates)
    print("Target:", target)
    print("Combinations:", sol.combinationSum2(candidates,target))
    print()

    # Test case 2
    candidates=[2,5,2,1,2]
    target=5
    print("Test Case 2:")
    print("Candidates:", candidates)
    print("Target:", target)
    print("Combinations:", sol.combinationSum2(candidates,target))
