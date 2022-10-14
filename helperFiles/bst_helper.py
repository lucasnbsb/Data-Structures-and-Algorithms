from collections import deque
import queue
from typing import List, Optional

from numpy import true_divide


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)
    
def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y-20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x-dx, y-60, dx/2)
            jumpto(x, y-20)
            draw(node.right, x+dx, y-60, dx/2)
    import turtle
    t = turtle.Turtle()
    t.speed(0); turtle.delay(0)
    h = height(root)
    jumpto(0, 30*h)
    draw(root, 0, 30*h, 40*h)
    t.hideturtle()
    turtle.mainloop()

def bfs(root):
    queue = deque()
    if root:
        queue.append(root)
    level = 0
    while len(queue) > 0:
        print("level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1


def rightSideView(root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if not root:
            return []
        res = []
        queue.append(root)
        firstInLevel = True
        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()
                if firstInLevel:
                    res.append(curr.val)
                    firstInLevel = False
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
            firstInLevel = True
        return res


def treverse(node, path, target):
    print(target)
    if not node:
        return False
    
    path.append(node.val)
    if not node.left and not node.right and sum(path) == target:
        return True
    if treverse(node.left, path, target):
        return True
    if treverse(node.right, path, target):
        return True
    path.pop()
    return False

def hasPathSum( root: Optional[TreeNode], targetSum: int) -> bool:
    path = []
    return treverse( root, path, targetSum)

if __name__ == '__main__':
    # deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]')
    # deserialize('[3,9,20,null,null,15,7]')
    # deserialize('[1,2,3,null,5,null,4]')
    # [5,4,8,11,null,13,4,7,2,null,null,null,1]

    root = deserialize('[5,4,8,11,null,13,4,7,2,null,null,null,1]')
    #drawtree(root)
    #root = deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]')
    print(hasPathSum(root, 22))
