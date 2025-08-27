from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(r, c, i):
            # if all chars matched
            if i == len(word):
                return True
            # invalid position or mismatch
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False

            # temporarily mark visited
            temp = board[r][c]
            board[r][c] = "#"

            # explore 4 directions
            found = (backtrack(r + 1, c, i + 1) or
                     backtrack(r - 1, c, i + 1) or
                     backtrack(r, c + 1, i + 1) or
                     backtrack(r, c - 1, i + 1))

            # restore original value
            board[r][c] = temp
            return found

        # try starting from each cell
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    board1 = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word1 = "ABCCED"
    print("Test Case 1:", solution.exist(board1, word1))  # Expected: True

    # Test Case 2
    board2 = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word2 = "SEE"
    print("Test Case 2:", solution.exist(board2, word2))  # Expected: True

    # Test Case 3
    board3 = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word3 = "ABCB"
    print("Test Case 3:", solution.exist(board3, word3))  # Expected: False
