from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self,val:int=0,left:'TreeNode'=None,right:'TreeNode'=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def zigzagLevelOrder(self,root:Optional[TreeNode])->List[List[int]]:

        if not root:
            return []

        queue=deque([root])
        result=[]
        left_to_right=True

        while queue:
            level_size=len(queue)
            level_nodes=[]

            for _ in range(level_size):
                node=queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not left_to_right:
                level_nodes.reverse()

            result.append(level_nodes)
            left_to_right=not left_to_right  # toggle direction

        return result


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


    root=build_tree([3, 9, 20, None, None, 15, 7])
    print(Solution().zigzagLevelOrder(root))
    # Expected Output: [[3], [20, 9], [15, 7]]
