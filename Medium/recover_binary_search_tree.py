from typing import Optional
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def recoverTree(self,root:Optional[TreeNode])->None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first=self.second=self.prev=None

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            # Detect swapped nodes
            if self.prev and self.prev.val>node.val:
                if not self.first:
                    self.first=self.prev
                self.second=node
            self.prev=node

            inorder(node.right)

        inorder(root)

        # Swap values of the two wrong nodes
        if self.first and self.second:
            self.first.val, self.second.val=self.second.val, self.first.val


if __name__=="__main__":
    sol=Solution()

    # Helper to build tree
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

    # Helper to get inorder list
    def inorder_list(root):
        if not root: return []
        return inorder_list(root.left)+[root.val]+inorder_list(root.right)

    # Test case
    root=build_tree([1,3,None,None,2])  # swapped nodes
    print("Before:", inorder_list(root))
    sol.recoverTree(root)
    print("After: ", inorder_list(root))  # Should be sorted inorder
