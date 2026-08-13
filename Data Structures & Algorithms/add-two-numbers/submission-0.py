# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        num1 = 0
        i = 0
        while curr1:
            num1 += curr1.val * (10 ** i)
            curr1 = curr1.next
            i += 1
        num2 = 0
        i = 0
        while curr2:
            num2 += curr2.val * (10 ** i)
            curr2 = curr2.next
            i += 1
        
        answer = num1 + num2
        dummy = ListNode()
        curr = dummy
        for c in str(answer)[::-1]:
            curr.next = ListNode(int(c))
            curr = curr.next

        return dummy.next
