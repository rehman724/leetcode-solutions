

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both until first reaches end
        while first:
            first = first.next
            second = second.next

        # Skip the node to be removed
        second.next = second.next.next

        return dummy.next


# Helper: build linked list from Python list
def build_linked_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


# Helper: convert linked list to Python list
def linked_list_to_list(head):
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


# Test cases
if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3], 3, [2, 3]),
    ]

    for i, (arr, n, expected) in enumerate(tests, 1):
        head = build_linked_list(arr)
        new_head = Solution().removeNthFromEnd(head, n)
        output = linked_list_to_list(new_head)
        status = "OK" if output == expected else "FAIL"
        print(f"Test {i}: Input={arr}, n={n} -> Output={output}, Expected={expected} [{status}]")
