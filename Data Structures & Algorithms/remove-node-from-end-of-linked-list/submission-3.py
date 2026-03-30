# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
        
        pos = length - n + 1

        curr = head
        prev = None

        if pos == 1:
            return head.next

        for i in range(pos - 1):
            prev = curr
            curr = curr.next

        prev.next = curr.next

        return head

