# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse the linked list twice
        # first reverse then remove nth element from head
        # then reverse again
        def reverseList(head: Optional[ListNode]):
            curr = head
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        reversedHead = reverseList(head)
        # remove the nth element
        if n == 1:
            reversedHead = reversedHead.next
            return reverseList(reversedHead)
        curr = reversedHead
        
        for i in range(1, n - 1):
            curr = curr.next
        
        if curr.next:
            curr.next = curr.next.next
        else: curr = None
        
        # reverse again
        newHead = reverseList(reversedHead)

        return newHead