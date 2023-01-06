class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        def dfs(root, maxVal):
            nonlocal good
            if not root: return
            
            if root.val >= maxVal:
                good += 1
                maxVal = root.val
            
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)

        dfs(root, float('-inf'))
        return good