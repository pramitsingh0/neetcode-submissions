# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(a, b):
            if not a and not b: return True
            elif not a and b: return False
            elif not b and a: return False
            else:
                return a.val == b.val and dfs(a.left, b.left) and dfs(a.right, b.right)
        
        return dfs(p, q)