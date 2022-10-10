class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        if self.head is None:
            return -1
        
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = self.head
        if(cur is None):
            self.head = Node(val,None)
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(val, None)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
        else:
            cur = self.head
            for i in range(index-1): #stop short to insert at i
                cur = cur.next
            node = Node(val, cur.next)
            cur.next = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        cur = self.head
        if(index == 0):
            self.head = cur.next
        else:
            for i in range(index-1):
                cur = cur.next
            cur.next = cur.next.next
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)