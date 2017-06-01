# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        dummy = ListNode('-inf')
        pre = dummy
        cur = head
        
        while cur:
            if cur.next and cur.val == cur.next.val:
                val = cur.val
                while cur and cur.val == val:  #####as long as you have the same values
                    cur = cur.next
                pre.next = cur
                
            else:
                pre.next = cur
                pre = cur     #####you have to update pre
                cur = cur.next
        
        return dummy.next
