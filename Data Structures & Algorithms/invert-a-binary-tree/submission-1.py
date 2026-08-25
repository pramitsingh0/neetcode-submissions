# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = root

        def invert(node):
            if not node:
                # we have reached the bottom
                return node
            iNodeLeft = invert(node.left)
            iNodeRight = invert(node.right)
            node.left = iNodeRight
            node.right = iNodeLeft
            return node
        
        return invert(root)


