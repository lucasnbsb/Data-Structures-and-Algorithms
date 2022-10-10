# Runtime: 325 ms, faster than 77.10% of Python3 online submissions for Design Browser History.
# Memory Usage: 16.6 MB, less than 65.27% of Python3 online submissions for Design Browser History.


class Node(object):
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage, None, None)

    def visit(self, url: str) -> None:
        node = Node(url, None, self.head)
        self.head.next = node
        self.head = node

    def back(self, steps: int) -> str:
        cur = self.head
        i = steps
        while cur.prev is not None and i > 0:
            cur = cur.prev
            i -= 1
        self.head = cur
        return self.head.val

    def forward(self, steps: int) -> str:
        cur = self.head
        i = steps
        while cur.next is not None and i>0:
            cur = cur.next
            i -= 1
        self.head = cur
        return self.head.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)