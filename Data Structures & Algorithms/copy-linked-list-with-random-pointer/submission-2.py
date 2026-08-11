"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {}

        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            currCopyNode = oldToCopy[curr]
            currCopyNode.next = oldToCopy[curr.next] if curr.next else None
            currCopyNode.random = oldToCopy[curr.random] if curr.random else None
            curr = curr.next
        return oldToCopy[head] if head else None