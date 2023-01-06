class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        # you dont have to keep traversing when you find one.
        def dfs(root):
            if not root or root == p or root == q: 
                return root
            left = dfs(root.left)
            right = dfs(root.right)
            if left and right: return root
            # and this is why. when you finish the traversal if only one is not null that one is the ancestor
            return left if left else right
        return dfs(root)