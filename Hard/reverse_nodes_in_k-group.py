# Definition for singly-linked list.
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next


class Solution:
    def reverseKGroup(self,head:ListNode,k:int)->ListNode:
        # Step 1: Count the total nodes
        count=0
        node=head
        while node:
            count+=1
            node=node.next

        # Step 2: Reverse k nodes at a time
        dummy=ListNode(0)
        dummy.next=head
        prev_group=dummy

        while count>=k:
            curr=prev_group.next
            next_node=curr.next

            # Reverse k-1 links
            for _ in range(1,k):
                curr.next=next_node.next
                next_node.next=prev_group.next
                prev_group.next=next_node
                next_node=curr.next

            # Move prev_group forward for next reversal
            prev_group=curr
            count-=k

        return dummy.next
