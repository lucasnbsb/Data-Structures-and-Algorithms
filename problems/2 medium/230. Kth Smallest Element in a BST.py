# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = k
        stack = []
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            counter -= 1
            if counter == 0:
                return stack.pop().val
            node = stack.pop()
            node = node.right
