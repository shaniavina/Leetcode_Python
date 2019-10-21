# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # o(1) space// o(nlgn) timeComplexity
        # bottom up, merge sort
        if head is None:
            return None
        
        def getSize(head):
            count = 0
            while head:
                count += 1
                head = head.next
            return count
        def split(head, step):
            i = 1
            while i < step and head:
                head = head.next
                i += 1
            if head is None:
                return None
            ### disconnect
            temp = head.next
            head.next = None
            return temp
        def merge(l, r, head):
            cur = head
            while l and r:
                if l.val < r.val:
                    cur.next = l
                    l = l.next
                else:
                    cur.next = r
                    r = r.next
                cur = cur.next
            cur.next = l if l is not None else r
            while cur.next is not None:
                cur = cur.next
            return cur
        
        size = getSize(head)
        bs = 1
        dummy = ListNode(0)
        dummy.next = head
        l, r, tail = None, None, None
        while bs < size:
            cur = dummy.next
            tail = dummy
            while cur:
                l = cur
                r = split(l, bs)
                cur = split(r, bs)
                tail = merge(l, r, tail)
            bs <<= 1
        return dummy.next
