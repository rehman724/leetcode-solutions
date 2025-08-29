
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current=head
        while current and current.next:
            if current.val==current.next.val:
                current.next=current.next.next  # Skip duplicate
            else:
                current=current.next
        return head

def list_to_linkedlist(arr:List[int])->Optional[ListNode]:
    """Convert Python list to Linked List."""
    if not arr:
        return None
    head=ListNode(arr[0])
    current=head
    for val in arr[1:]:
        current.next=ListNode(val)
        current=current.next
    return head

def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    """Convert Linked List back to Python list."""
    result=[]
    current=head
    while current:
        result.append(current.val)
        current=current.next
    return result

if __name__=="__main__":
    solution = Solution()

    # Test Case 1
    head=list_to_linkedlist([1,1,2])
    result=solution.deleteDuplicates(head)
    print("Input: [1,1,2] => Output:", linkedlist_to_list(result))  # [1,2]

    # Test Case 2
    head=list_to_linkedlist([1,1,2,3,3])
    result=solution.deleteDuplicates(head)
    print("Input: [1,1,2,3,3] => Output:", linkedlist_to_list(result))  # [1,2,3]
