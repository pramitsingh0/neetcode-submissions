# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        l = dummy
        r = None
        curr = dummy
        for i in range(n):
            curr = curr.next
        r = curr
        while r.next:
            r = r.next
            l = l.next
        if l and l.next:
            l.next = l.next.next
        
        return dummy.next
