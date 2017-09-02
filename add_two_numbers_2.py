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
        stk1, stk2 = [], []
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        while l2:
            stk2.append(l2.val)
            l2 = l2.next
        
       
        pre, cur, sum = None, None, 0
        while stk1 or stk2:
            if stk1:
                sum += stk1.pop()
            if stk2:
                sum += stk2.pop()
                
            cur = ListNode(sum % 10)
            cur.next = pre
            pre = cur
            sum /= 10
        if sum:
            cur = ListNode(sum)
            cur.next = pre
        return cur
            
