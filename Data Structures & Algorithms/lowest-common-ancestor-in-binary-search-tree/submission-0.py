# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root
        # if p and q belong to the same subtree, we need to go deeper as there can be a lower common ancestor
        # but the moment p and q belong to different sub tree we know that we have found the common ancestor
        if not root.left or not root.right: return root

        if ((root.val >= p.val and root.val <= q.val) or
            (root.val <= p.val and root.val >= q.val)):
            return root
        elif (p.val <= root.val and q.val <= root.val):
            # then we search in left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        elif (p.val >= root.val and q.val >= root.val):
            return self.lowestCommonAncestor(root.right, p, q)

        return res