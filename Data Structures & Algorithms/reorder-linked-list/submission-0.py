# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # first we find the mid point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # we split the list
        second = slow.next
        prev = slow.next = None

        # we reverse the list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        second = prev
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

        


        # first we find mid point of list
