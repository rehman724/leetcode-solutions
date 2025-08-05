# Easy/two_sum.py

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# Example test
if __name__ == "__main__":
    result = twoSum([2, 7, 11, 15], 9)
    print("Indices:", result)  # Output: [0, 1]
