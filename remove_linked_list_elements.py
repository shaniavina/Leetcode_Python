# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(float('-inf'))
        dummy.next = head
        pre, curr = dummy, dummy.next
        
        while curr:
            if curr.val == val:
                pre.next = curr.next
            else:
                pre = curr
            curr = curr.next
        return dummy.next
    
    
@@@@@@@myself
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
            
        dummy = ListNode('-inf')
        pre = dummy
        cur = head
        
        while cur:
            if cur.val == val:
                pre.next = cur.next
               
                cur = cur.next
            else:
                pre.next = cur
                pre = cur
                cur = cur.next
        return dummy.next
                
                
