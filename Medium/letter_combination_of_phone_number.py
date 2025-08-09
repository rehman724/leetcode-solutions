# Problem: Letter Combinations of a Phone Number


class Solution(object):
    def letterCombinations(self,digits):

        if not digits:
            return []

        phone_map = {
            "2":"abc","3":"def","4":"ghi","5":"jkl",
            "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }

        result = []

        def backtrack(index,current):
            if index == len(digits):
                result.append(current)
                return

            for letter in phone_map[digits[index]]:
                backtrack(index+1,current+letter)

        backtrack(0, "")
        return result


# Example usage:
if __name__=="__main__":
    solution=Solution()
    digits="23"
    print(solution.letterCombinations(digits))  # Expected Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
