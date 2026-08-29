# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        stack = [[root]]
        res = []
        
        while stack:
            row = stack.pop()
            newResRow = []
            newStackRow = []
            for node in row:
                if not node: break
                newResRow.append(node.val)
                if node.left:
                    newStackRow.append(node.left)
                if node.right:
                    newStackRow.append(node.right)
                

            if newResRow:
                res.append(newResRow)
            if newStackRow:
                stack.append(newStackRow)
        return res