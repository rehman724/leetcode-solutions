from typing import Optional
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def isValidBST(self,root:Optional[TreeNode])->bool:
        def helper(node,low=float('-inf'),high=float('inf')):
            if not node:
                return True
            if not (low<node.val<high):
                return False
            return (helper(node.left,low,node.val) and
                    helper(node.right,node.val,high))
        return helper(root)


# ----------------- TESTING -----------------
if __name__=="__main__":
    sol=Solution()

    # Helper function to build tree
    def build_tree(nodes):
        """Builds tree from level-order list (None for empty)."""
        if not nodes:
            return None
        from collections import deque
        root=TreeNode(nodes[0])
        q=deque([root])
        i=1
        while q and i<len(nodes):
            curr=q.popleft()
            if nodes[i] is not None:
                curr.left=TreeNode(nodes[i])
                q.append(curr.left)
            i+=1
            if i<len(nodes) and nodes[i] is not None:
                curr.right=TreeNode(nodes[i])
                q.append(curr.right)
            i+=1
        return root

    test_cases=[
        ([2,1,3],True),                  # Valid BST
        ([5,1,4,None,None,3,6],False), # Invalid BST
        ([1,1],False),                   # Duplicate not allowed
        ([10,5,15,None,None,6,20],False),
        ([3,1,5,0,2,4,6],True),
        ([],True),                        # Empty tree is valid
    ]

    for i, (nodes,expected) in enumerate(test_cases,1):
        root=build_tree(nodes)
        result=sol.isValidBST(root)
        print(f"Test Case {i}: {nodes} → {result} "
              f"{' PASS' if result == expected else ' FAIL'}")
