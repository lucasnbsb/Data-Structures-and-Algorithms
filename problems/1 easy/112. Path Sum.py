# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treverse(self,node, path, target):
        if not node:
            return False
        path.append(node.val)
        if not node.left and not node.right and sum(path) == target:
            return True
        if self.treverse(node.left, path, target):
            return True
        if self.treverse(node.right, path, target):
            return True
        path.pop()
        return False
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path = []
        return self.treverse(root, path, targetSum)