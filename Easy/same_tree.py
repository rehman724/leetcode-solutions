from typing import Optional
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def isSameTree(self,p:Optional[TreeNode],q:Optional[TreeNode])->bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


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
        ([1,2,3],[1,2,3],True),
        ([1,2],[1,None,2],False),
        ([1,2,1],[1,1,2],False),
        ([], [],True),
    ]

    for i, (tree1,tree2,expected) in enumerate(test_cases,1):
        p=build_tree(tree1)
        q=build_tree(tree2)
        result=sol.isSameTree(p,q)
        print(f"Test Case {i}: {tree1} vs {tree2} → {result} "
              f"{' PASS' if result == expected else ' FAIL'}")
