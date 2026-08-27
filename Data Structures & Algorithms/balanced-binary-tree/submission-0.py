# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        node = root
        if not node: return True
        heightL = self.height(node.left)
        heightR = self.height(node.right)

        return (abs(heightL - heightR) <= 1) and self.isBalanced(node.left) and self.isBalanced(node.right)

    def height(self, node):
        if not node: return 0
        return 1 + max(self.height(node.left), self.height(node.right))