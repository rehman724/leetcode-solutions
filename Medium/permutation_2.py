from typing import List


class Solution:
    def permuteUnique(self,nums:List[int])->List[List[int]]:
        nums.sort()
        result=[]
        used = [False]*len(nums)

        def backtrack(current):
            if len(current)==len(nums):
                result.append(current[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                used[i]=True
                current.append(nums[i])
                backtrack(current)
                current.pop()
                used[i]=False

        backtrack([])
        return result

if __name__=="__main__":
    sol=Solution()

    # Test 1
    nums1 = [1,1,2]
    print("Input:", nums1)
    print("Unique Permutations:", sol.permuteUnique(nums1))
    # Expected: [[1,1,2],[1,2,1],[2,1,1]]

    # Test 2
    nums2 = [1,2,3]
    print("\nInput:", nums2)
    print("Unique Permutations:", sol.permuteUnique(nums2))
    # Expected: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    # Test 3
    nums3 = [2,2,1,1]
    print("\nInput:", nums3)
    print("Unique Permutations:", sol.permuteUnique(nums3))
    # Expected: [[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]]
