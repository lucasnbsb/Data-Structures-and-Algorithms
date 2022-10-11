from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderSucessor(self, root: Optional[TreeNode], k: int) -> int:
        sucessor = None
        while root:
            if k >= root.val:
                root = root.right
            else:
                sucessor = root
                root = root.right
        return sucessor
