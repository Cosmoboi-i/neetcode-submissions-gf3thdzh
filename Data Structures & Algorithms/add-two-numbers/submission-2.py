# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1 = l1
        cur2 = l2

        carry = 0
        while cur1 and cur2:
            sum = cur1.val + cur2.val + carry
            carry = sum // 10
            cur1.val = sum % 10
            prev1 = cur1
            prev2 = cur2
            cur1 = cur1.next
            cur2 = cur2.next
        
        if cur1:
            while carry and cur1:
                sum = cur1.val + carry
                carry = sum // 10
                cur1.val = sum % 10
                prev1 = cur1
                cur1 = cur1.next
        elif cur2:
            prev1.next = cur2
            while carry and cur2:
                sum = cur2.val + carry
                carry = sum // 10
                cur2.val = sum % 10
                prev2 = cur2
                cur2 = cur2.next
            prev1 = prev2

        if carry:
            node = ListNode(1)
            prev1.next = node
        
        return l1


