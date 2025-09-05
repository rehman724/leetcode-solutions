from typing import Optional
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def isSymmetric(self,root:Optional[TreeNode])->bool:
        if not root:
            return True

        def isMirror(t1,t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val==t2.val and
                    isMirror(t1.left,t2.right) and
                    isMirror(t1.right,t2.left))

        return isMirror(root.left,root.right)


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
            if i<len(nodes) and nodes[i] is not None:
                curr.left=TreeNode(nodes[i])
                q.append(curr.left)
            i+=1
            if i<len(nodes) and nodes[i] is not None:
                curr.right=TreeNode(nodes[i])
                q.append(curr.right)
            i+=1
        return root

    test_cases=[
        ([1,2,2,3,4,4,3],True),           # Symmetric
        ([1,2,2,None,3,None,3],False),    # Not symmetric
        ([1,2,2,2,None,2],False),         # Not symmetric
        ([],True),                        # Empty tree is symmetric
    ]

    for i,(tree,expected) in enumerate(test_cases,1):
        root=build_tree(tree)
        result=sol.isSymmetric(root)
        print(f"Test Case {i}: {tree} → {result} "
              f"{' PASS' if result == expected else ' FAIL'}")
