"""
Description:
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed).

Example:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Approach:
We use a dummy node to simplify pointer manipulation and
iteratively swap every two nodes in the list.
"""

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def swapPairs(head:ListNode)->ListNode:
    dummy=ListNode(0)
    dummy.next=head
    prev=dummy

    while prev.next and prev.next.next:
        first=prev.next
        second=first.next

        # Swapping nodes
        prev.next=second
        first.next=second.next
        second.next=first

        # Move prev two steps forward
        prev=first

    return dummy.next
def list_to_linkedlist(lst):
    dummy=ListNode(0)
    current=dummy
    for val in lst:
        current.next=ListNode(val)
        current=current.next
    return dummy.next

def linkedlist_to_list(node):
    lst=[]
    while node:
        lst.append(node.val)
        node=node.next
    return lst

if __name__=="__main__":
    test_cases=[
        ([1,2,3,4],[2,1,4,3]),
        ([],[]),
        ([1],[1]),
        ([1,2,3],[2,1,3])
    ]

    for i, (inp,expected) in enumerate(test_cases,1):
        head=list_to_linkedlist(inp)
        result=swapPairs(head)
        result_list=linkedlist_to_list(result)
        print(f"Test Case {i}: Input={inp} → Output={result_list} | Expected={expected}")
        assert result_list==expected

    print("All test cases passed")
