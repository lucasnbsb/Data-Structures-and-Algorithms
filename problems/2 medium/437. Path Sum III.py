# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    output = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        res = [targetSum]
        def dfs(node, sumTracking):
            if not node:
                return 0
            next = [targetSum]
            for sum in sumTracking:
                if (sum-node.val == 0):
                    self.output += 1
                next.append(sum - node.val)
            dfs(node.left, next)
            dfs(node.right, next)
        dfs(root, res)
        return self.output