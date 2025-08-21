from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next


class Solution:
    def rotateRight(self,head:Optional[ListNode],k:int)->Optional[ListNode]:
        if not head or not head.next or k==0:
            return head

        # Step 1: Find the length of the list
        length=1
        current=head
        while current.next:
            current=current.next
            length+=1

        # Step 2: Make it circular
        current.next=head

        # Step 3: Find new head position
        k=k%length
        steps_to_new_head=length-k

        new_tail=head
        for _ in range(steps_to_new_head-1):
            new_tail=new_tail.next

        new_head=new_tail.next
        new_tail.next=None

        return new_head

def build_linked_list(values):
    if not values:
        return None
    head=ListNode(values[0])
    current=head
    for val in values[1:]:
        current.next=ListNode(val)
        current=current.next
    return head


def linked_list_to_list(head):
    result=[]
    while head:
        result.append(head.val)
        head=head.next
    return result


# ------------------- TEST CASES -------------------
if __name__=="__main__":
    sol=Solution()

    # Example 1
    head=build_linked_list([1,2,3,4,5])
    result=sol.rotateRight(head, 2)
    print("Test 1:", linked_list_to_list(result))  # Expected [4, 5, 1, 2, 3]

    # Example 2
    head=build_linked_list([0,1,2])
    result=sol.rotateRight(head, 4)
    print("Test 2:", linked_list_to_list(result))  # Expected [2, 0, 1]

    # Edge case: Single element
    head=build_linked_list([1])
    result=sol.rotateRight(head, 10)
    print("Test 3:", linked_list_to_list(result))  # Expected [1]

    # Edge case: Empty list
    head=build_linked_list([])
    result=sol.rotateRight(head, 1)
    print("Test 4:", linked_list_to_list(result))  # Expected []
