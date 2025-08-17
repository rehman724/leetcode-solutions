# Filename: group_anagrams.py

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            # Sort the word and use it as the key
            key = ''.join(sorted(word))
            anagram_map[key].append(word)

        return list(anagram_map.values())


# ----------- Test Code -------------
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Input:", strs)
    print("Grouped Anagrams:", solution.groupAnagrams(strs))
    # Expected output: [["eat","tea","ate"],["tan","nat"],["bat"]]

    # Test case 2
    strs = [""]
    print("\nInput:", strs)
    print("Grouped Anagrams:", solution.groupAnagrams(strs))
    # Expected output: [[""]]

    # Test case 3
    strs = ["a"]
    print("\nInput:", strs)
    print("Grouped Anagrams:", solution.groupAnagrams(strs))
    # Expected output: [["a"]]
