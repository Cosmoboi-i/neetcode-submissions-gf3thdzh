# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        
        curr = head
        count = 0

        while curr:
            count += 1
            curr = curr.next
        
        endList = head
        for i in range(int((count + 1) / 2) - 1):
            endList = endList.next
        
        second = endList.next
        endList.next = None
        
        endHead = self.reverseList(second)

        curr = head
        endCurr = endHead

        while endCurr:
            nxt = curr.next
            curr.next = endCurr
            endNxt = endCurr.next
            endCurr.next = nxt
            curr = nxt
            endCurr = endNxt






