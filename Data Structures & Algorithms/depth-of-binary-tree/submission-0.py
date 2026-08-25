# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        height = 0

        def goDeep(node):
            if not node:
                return 0
            height = 1 + max(goDeep(node.left), goDeep(node.right))
            return height
        return goDeep(root)