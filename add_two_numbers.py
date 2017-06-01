# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode('-inf')
        cur, carry = dummy, 0
        
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            val, carry = val % 10, val / 10
            cur.next = ListNode(val)
            cur = cur.next
            
        if carry == 1:
            cur.next = ListNode(1)
            
        return dummy.next
        
            
