class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        nodes = collections.defaultdict(ListNode)
        size = 0
        while cur:
            nodes[size] = cur
            cur = cur.next
            size += 1
        
        if size <= 2:
            return

        anchor = ListNode()
        for i in range(size//2):
            nodes[i].next = nodes[size-i-1]
            nodes[size-i-1].next = nodes[i+1]

        nodes[(size//2)].next = None