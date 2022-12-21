class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        start = Node(0)
        last = start
        mapping = {}
        current = head
        while current is not None:
            tmp = Node(current.val)
            last.next = tmp
            last = tmp
            mapping[current] = tmp
            current = current.next
        
        current = head
        while current is not None:
            if current.random is not None:
                mapping[current].random = mapping[current.random]
            current = current.next
        return start.next