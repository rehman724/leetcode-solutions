from typing import Optional, List
class ListNode:
    def __init__(self,val:int=0,next:Optional['ListNode']=None):
        self.val =val
        self.next=next

    def __repr__(self):
        return f"{self.val}->{self.next}"


class Solution:
    def deleteDuplicates(self,head:Optional[ListNode])->Optional[ListNode]:
        dummy=ListNode(0,head)
        prev=dummy
        current=head

        while current:
            # Detect duplicates
            if current.next and current.val==current.next.val:
                # Skip all nodes with same value
                while current.next and current.val==current.next.val:
                    current=current.next
                prev.next=current.next
            else:
                prev=prev.next
            current=current.next

        return dummy.next


def build_linked_list(values:List[int])->Optional[ListNode]:
    if not values:
        return None
    head=ListNode(values[0])
    current=head
    for val in values[1:]:
        current.next=ListNode(val)
        current=current.next
    return head


def linked_list_to_list(head:Optional[ListNode])->List[int]:
    result=[]
    while head:
        result.append(head.val)
        head=head.next
    return result


if __name__=="__main__":
    sol=Solution()

    # Example 1
    head=build_linked_list([1,2,3,3,4,4,5])
    print(linked_list_to_list(sol.deleteDuplicates(head)))  # Expected: [1,2,5]

    # Example 2
    head=build_linked_list([1,1,1,2,3])
    print(linked_list_to_list(sol.deleteDuplicates(head)))  # Expected: [2,3]

