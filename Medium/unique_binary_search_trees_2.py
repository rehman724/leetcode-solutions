from typing import List, Optional
from collections import deque


# Define TreeNode (since GitHub/local doesn't provide it)
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def generateTrees(self,n:int)->List[Optional[TreeNode]]:
        if n==0:
            return []

        def build_trees(start,end):
            if start>end:
                return [None]
            all_trees=[]
            for i in range(start,end+1):
                left_trees=build_trees(start,i-1)
                right_trees=build_trees(i+1,end)
                for l in left_trees:
                    for r in right_trees:
                        root=TreeNode(i)
                        root.left=l
                        root.right=r
                        all_trees.append(root)
            return all_trees

        return build_trees(1,n)


# Helper: Serialize tree to list (like LeetCode format)
def serialize(root: Optional[TreeNode])->List[Optional[int]]:
    if not root:
        return []
    result=[]
    queue=deque([root])
    while queue:
        node=queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result


if __name__=="__main__":
    sol=Solution()
    trees=sol.generateTrees(3)

    print(f"Total unique BSTs for n=3: {len(trees)}")
    for idx,t in enumerate(trees, 1):
        print(f"Tree {idx}: {serialize(t)}")
