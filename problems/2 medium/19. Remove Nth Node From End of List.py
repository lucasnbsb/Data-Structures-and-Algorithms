# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        anotherDummy = dummy = head
        nodes = []
        while head != None:
            nodes.append(head)
            head = head.next
        
        if n == len(nodes):
            return dummy.next
        elif n == 1:
            nodes[-2].next = None
        else:
            nodes[-(n+1)].next = nodes[-(n-1)]
        return dummy