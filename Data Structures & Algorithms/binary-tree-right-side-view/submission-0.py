# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        layers = []
        res = []
        queue = collections.deque()

        if root:
            queue.append(root)
        
        level = 0
        while len(queue) > 0:
            queLen = len(queue)
            if len(layers) == level: layers.append([])
            for i in range(queLen):
                node = queue.popleft()
                layers[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        for layer in layers:
            res.append(layer[-1])
            

        return res
