from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy  # Node right before the current group
        
        while True:
            # 1. Find the k-th node from groupPrev
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    break
            
            # If fewer than k nodes remain, we are done!
            if not kth:
                break
                
            groupNext = kth.next  # First node of the NEXT group
            
            # 2. Reverse the current group
            prev = groupNext  # Point original first node (1) to groupNext (3)
            curr = groupPrev.next
            
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # 3. Connect groupPrev to the new head of this reversed segment (kth)
            tmp = groupPrev.next  # Node 1 (which is now the tail of this group)
            groupPrev.next = kth  # groupPrev now points to Node 2
            groupPrev = tmp       # Move groupPrev to Node 1 for the next iteration
            
        return dummy.next

def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res

obj = Solution()
head = build_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
result_head = obj.reverseKGroup(head=head, k=3)
print(linked_list_to_list(result_head))