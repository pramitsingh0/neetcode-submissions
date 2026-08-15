# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        leftPrev = dummy
        curr = head
        # we store the left previous, and we get to the start
        # of the index from where we need to reverse
        for i in range(left - 1):
            curr = curr.next
            leftPrev = leftPrev.next
        
        # then we reverse the section between left and right inclusive
        prev = None
        for i in range(right - left + 1):
            tempNext = curr.next
            curr.next = prev
            prev, curr = curr, tempNext
        
        # here prev points to end of the section that we just rotated
        # cur points to node just after the ned
        leftPrev.next.next = curr
        leftPrev.next = prev

        return dummy.next
        
        

