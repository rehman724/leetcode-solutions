from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)

        return res


# ----------------- TESTING -----------------
if __name__ == "__main__":
    sol = Solution()

    # Helper function to build tree
    def build_tree(nodes):
        """Builds tree from level-order list (None for empty)."""
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        q = deque([root])
        i = 1
        while q and i < len(nodes):
            curr = q.popleft()
            if i < len(nodes) and nodes[i] is not None:
                curr.left = TreeNode(nodes[i])
                q.append(curr.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                curr.right = TreeNode(nodes[i])
                q.append(curr.right)
            i += 1
        return root

    test_cases = [
        ([3,9,20,None,None,15,7], [[3],[9,20],[15,7]]),
        ([1], [[1]]),
        ([], []),
        ([1,2,3,4,None,None,5], [[1],[2,3],[4,5]]),
    ]

    for i, (tree, expected) in enumerate(test_cases, 1):
        root = build_tree(tree)
        result = sol.levelOrder(root)
        print(f"Test Case {i}: {tree} → {result} "
              f"{'PASS' if result == expected else 'FAIL'}")
