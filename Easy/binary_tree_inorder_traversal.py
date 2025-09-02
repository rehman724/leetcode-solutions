from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def inorderTraversal(self,root:Optional[TreeNode])->List[int]:
        """
        Perform inorder traversal (Left -> Root -> Right) using iterative approach.
        """
        result=[]
        stack=[]
        current=root

        while current or stack:
            while current:
                stack.append(current)
                current=current.left
            current=stack.pop()
            result.append(current.val)
            current=current.right

        return result


if __name__=="__main__":
    # Helper function to build binary tree from list (for testing)
    def build_tree(values):
        if not values:
            return None
        nodes=[TreeNode(val) if val is not None else None for val in values]
        kids=nodes[::-1]
        root=kids.pop()
        for node in nodes:
            if node:
                if kids: node.left=kids.pop()
                if kids: node.right=kids.pop()
        return root

    # Test Case 1
    root1=build_tree([1, None, 2, 3])
    print(Solution().inorderTraversal(root1))  # Expected: [1, 3, 2]

    # Test Case 2
    root2=build_tree([])
    print(Solution().inorderTraversal(root2))  # Expected: []

