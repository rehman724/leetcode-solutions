from typing import Optional
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def partition(self,head:Optional[ListNode],x:int)->Optional[ListNode]:
        # Two dummy heads for small and large lists
        small_dummy=ListNode(0)
        large_dummy=ListNode(0)

        small=small_dummy
        large=large_dummy

        current=head
        while current:
            if current.val<x:
                small.next=current
                small=small.next
            else:
                large.next=current
                large=large.next
            current=current.next

        # Link the two lists
        large.next=None
        small.next=large_dummy.next

        return small_dummy.next


def build_linked_list(values):
    dummy=ListNode(0)
    curr=dummy
    for v in values:
        curr.next=ListNode(v)
        curr=curr.next
    return dummy.next

def linked_list_to_list(head):
    result=[]
    while head:
        result.append(head.val)
        head=head.next
    return result


if __name__=="__main__":
    solver=Solution()

    # Example 1
    head1=build_linked_list([1,4,3,2,5,2])
    result1=solver.partition(head1, 3)
    print(linked_list_to_list(result1))  # Expected: [1,2,2,4,3,5]

    # Example 2
    head2=build_linked_list([2,1])
    result2=solver.partition(head2, 2)
    print(linked_list_to_list(result2))  # Expected: [1,2]

