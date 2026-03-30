# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()

        curr = head

        print(lists)
        count = 10

        while not all(x is None for x in lists):
            minVal = 1001
            minPtr = None
            minIndex = None
            for index, x in enumerate(lists):
                if x == None:
                    continue
                if x.val <= minVal:
                    minVal = x.val
                    minPtr = x
                    minIndex = index
            
            curr.next = minPtr
            curr = curr.next
            lists[minIndex] = minPtr.next
            
        return head.next

