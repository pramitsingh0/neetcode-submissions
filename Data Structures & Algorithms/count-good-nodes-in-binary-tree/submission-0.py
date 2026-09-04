# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = collections.deque([(root, float("-inf"))])

        while q:
            qLen = len(q)
            for i in range(qLen):
                node, maxVal = q.popleft()
                if node.val >= maxVal:
                    res += 1
                    maxVal = node.val
                if node.left:
                    q.append((node.left, maxVal))
                if node.right:
                    q.append((node.right, maxVal))
        return res