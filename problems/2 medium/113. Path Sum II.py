# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node, path, n):
            if not node:
                return[]
            path.append(node.val)
            if not node.left and not node.right and n == node.val:
                res.append(path[:])
            dfs(node.left, path, n-node.val)
            dfs(node.right, path, n-node.val)
            path.pop()
            
        dfs(root, [], targetSum)
        return res