import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        vals = []
        cur = self
        while cur:
            vals.append(str(cur.val))
            cur = cur.next
        return "->".join(vals)

def mergeKLists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    curr = dummy
    while heap:
        val, idx, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, idx, node.next))
    return dummy.next

# helpers
def create_linked_list(arr):
    dummy = ListNode()
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

if __name__ == "__main__":
    l1 = create_linked_list([1,4,5])
    l2 = create_linked_list([1,3,4])
    l3 = create_linked_list([2,6])
    merged = mergeKLists([l1, l2, l3])
    print("Merged:", merged)  # Merged: 1->1->2->3->4->4->5->6
