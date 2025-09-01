class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

    def __repr__(self):
        return f"{self.val}->{self.next}"


class Solution:
    def reverseBetween(self,head:ListNode,left:int,right:int)->ListNode:
        """
        Reverse sublist between left and right using iterative approach.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head or left==right:
            return head

        dummy=ListNode(0)
        dummy.next=head
        prev=dummy

        # Step 1: Move prev to node just before "left"
        for _ in range(left-1):
            prev=prev.next

        # Step 2: Reverse the sublist
        curr=prev.next
        nxt=None
        for _ in range(right-left):
            nxt=curr.next
            curr.next=nxt.next
            nxt.next=prev.next
            prev.next=nxt

        return dummy.next



# Helper functions for testing

def build_linked_list(values):
    dummy=ListNode(0)
    curr=dummy
    for val in values:
        curr.next=ListNode(val)
        curr=curr.next
    return dummy.next


def linked_list_to_list(head):
    result=[]
    while head:
        result.append(head.val)
        head=head.next
    return result


if __name__=="__main__":
    sol=Solution()

    # Example test cases
    head=build_linked_list([1,2,3,4,5])
    assert linked_list_to_list(sol.reverseBetween(head, 2, 4))==[1,4,3,2,5]

    head=build_linked_list([5])
    assert linked_list_to_list(sol.reverseBetween(head, 1, 1))==[5]

    print("All test cases passed!")
