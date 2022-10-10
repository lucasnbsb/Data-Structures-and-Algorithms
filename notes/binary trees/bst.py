from re import search


class TreeNode:
    def __init__(self, val):
        self.val = val;
        self.left = None
        self.right = None

# left is always less
# right is always greater
# O(h), O(log n) for a balanced tree

    def search(root, target):
        if not root:
            return False
        
        if target > root.val:
            return search(root.right, target)
        elif target < root.val: 
            return search(root.left, target)
        else:
            return True