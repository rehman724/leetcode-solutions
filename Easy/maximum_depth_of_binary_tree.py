from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self,val:int=0,left:'TreeNode'=None,right:'TreeNode'=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def maxDepth(self,root:Optional[TreeNode])->int:

        if not root:
            return 0
        left_depth=self.maxDepth(root.left)
        right_depth=self.maxDepth(root.right)
        return 1+max(left_depth, right_depth)


# ---------- Example Usage (local test) ----------
if __name__=="__main__":
    # Helper to build a tree from list input
    def build_tree(nodes):
        if not nodes: return None
        root=TreeNode(nodes[0])
        queue=deque([root])
        i=1
        while queue and i<len(nodes):
            node=queue.popleft()
            if nodes[i] is not None:
                node.left=TreeNode(nodes[i])
                queue.append(node.left)
            i+=1
            if i<len(nodes) and nodes[i] is not None:
                node.right=TreeNode(nodes[i])
                queue.append(node.right)
            i+=1
        return root


    # Test Example
    root=build_tree([3,9,20,None,None,15,7])
    print(Solution().maxDepth(root))
    # Expected Output: 3
