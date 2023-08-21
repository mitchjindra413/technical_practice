# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        curr = dummy
        carry = 0
        
        while l1 and l2:
            new = l1.val + l2.val + carry
            tens, ones = divmod(new, 10)
            curr.next = ListNode(ones)
            carry = tens
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            new = l1.val + carry
            tens, ones = divmod(new, 10)
            curr.next = ListNode(ones)
            carry = tens
            curr = curr.next
            l1 = l1.next
            
        while l2:
            new = l2.val + carry
            tens, ones = divmod(new, 10)
            curr.next = ListNode(ones)
            carry = tens
            curr = curr.next
            l2 = l2.next
        
        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummy.next