def permute(nums):
    result = []
    used = [False] * len(nums)

    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                current.append(nums[i])
                backtrack(current)
                current.pop()
                used[i] = False

    backtrack([])
    return result


# ---------------------------
# Test Cases
# ---------------------------
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]),
        ([0, 1], [
            [0, 1],
            [1, 0]
        ]),
        ([1], [
            [1]
        ])
    ]

    for nums, expected in test_cases:
        result = permute(nums)
        print(f"nums: {nums} | Expected: {expected} | Got: {result} | Pass: {sorted(result) == sorted(expected)}")