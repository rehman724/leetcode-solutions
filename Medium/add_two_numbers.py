# Medium/add_two_numbers.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

def addTwoNumbers(l1,l2):
    dummy=ListNode()
    current=dummy
    carry=0

    while l1 or l2 or carry:
        val1=l1.val if l1 else 0
        val2=l2.val if l2 else 0

        total=val1+val2 +carry
        carry=total//10
        current.next=ListNode(total%10)

        current=current.next
        if l1:
            l1=l1.next
        if l2:
            l2=l2.next

    return dummy.next

# Optional: Helper function to print the result list
def printList(node):
    while node:
        print(node.val,end=" -> " if node.next else "\n")
        node=node.next

# Optional: Test example
if __name__=="__main__":
    # 342 + 465 = 807 => 7 -> 0 -> 8
    l1=ListNode(2,ListNode(4,ListNode(3)))
    l2=ListNode(5,ListNode(6,ListNode(4)))
    result=addTwoNumbers(l1,l2)
    printList(result)
