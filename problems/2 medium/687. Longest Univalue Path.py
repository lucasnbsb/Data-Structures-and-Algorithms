# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longestEver = 0
        def dfs(node):
            if not node:
                return 0

            leftPath = dfs(node.left)
            rightPath = dfs(node.right)

            leftRes = leftPath+1 if node.left and node.left.val == node.val else 0
            rightRes = rightPath+1 if node.right and node.right.val == node.val else 0

            nonlocal longestEver
            longestEver = max(longestEver, leftRes+rightRes)
            return max(leftRes, rightRes)
        dfs(root)
        return longestEver