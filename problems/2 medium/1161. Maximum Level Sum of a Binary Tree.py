# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        q = deque()
        if root:
            q.append(root)
        maxSum = float('-inf')
        maxLevel = 1
        level = 1
        while len(q) > 0:
            runningSum = 0
            for i in range(len(q)):
                curr = q.popleft()
                runningSum += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if runningSum > maxSum:
                maxLevel = level
                maxSum = runningSum
            level += 1
        return maxLevel