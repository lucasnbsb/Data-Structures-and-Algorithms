# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None"""  """

class Codec:

    def serialize(self, root):
        if not root: return ''

        output = []
        def dfs(root):
            if not root:
                output.append('n')
                return
            output.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return ','.join(output)

    def deserialize(self, data):
        if not data: return None
        tree = data.split(',')
        index = 0
        def dfs():
            nonlocal index
            if tree[index] == 'n':
                index += 1
                return None
            root = TreeNode(int(tree[index]))
            index += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))