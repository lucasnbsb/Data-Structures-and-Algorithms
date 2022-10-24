# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxHeight = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, h):
            if not node:
                return
            if self.maxHeight < h and not node.left and not node.right:
                self.maxHeight = h
            dfs(node.left, h+1)
            dfs(node.right, h+1)
        dfs(root, 1)
        return self.maxHeight