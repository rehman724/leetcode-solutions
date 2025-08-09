class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def mergeTwoLists(list1,list2):
    dummy=ListNode()
    current=dummy

    while list1 and list2:
        if list1.val<list2.val:
            current.next=list1
            list1=list1.next
        else:
            current.next=list2
            list2=list2.next
        current=current.next

    if list1:
        current.next=list1
    else:
        current.next=list2

    return dummy.next

# Helper function to convert Python list to linked list
def list_to_linkedlist(lst):
    dummy=ListNode()
    current=dummy
    for val in lst:
        current.next=ListNode(val)
        current=current.next
    return dummy.next

# Helper function to convert linked list to Python list
def linkedlist_to_list(node):
    result=[]
    while node:
        result.append(node.val)
        node=node.next
    return result

def main():
    # Test Case 1
    list1=list_to_linkedlist([1,2,4])
    list2=list_to_linkedlist([1,3,4])
    merged=mergeTwoLists(list1,list2)
    print("Test Case 1:",linkedlist_to_list(merged))  # Expected: [1, 1, 2, 3, 4, 4]

    # Test Case 2
    list1=list_to_linkedlist([])
    list2=list_to_linkedlist([])
    merged=mergeTwoLists(list1,list2)
    print("Test Case 2:",linkedlist_to_list(merged))  # Expected: []

    # Test Case 3
    list1=list_to_linkedlist([])
    list2=list_to_linkedlist([0])
    merged=mergeTwoLists(list1,list2)
    print("Test Case 3:",linkedlist_to_list(merged))  # Expected: [0]

if __name__=="__main__":
    main()
