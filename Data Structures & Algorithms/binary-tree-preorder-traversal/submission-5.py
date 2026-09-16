# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        stack = []
        res = []
        while cur or stack:
            while cur:
                stack.append(cur.right)
                res.append(cur.val)
                cur = cur.left
            cur = stack.pop()
        return res