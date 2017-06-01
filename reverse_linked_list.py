# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ####my edition: iteratively
        dummy = ListNode('-inf')
        while head:
            head.next, dummy.next, head = dummy.next, head, head.next
            
        return dummy.next

# Time:  O(n)
# Space: O(n)
# Recursive solution.  

class Solution:
    
    def reverseList(self, head):
        return self.doReverse(head, None)
    def doReverse(self, head, newHead):
        if head is None:
            return newHead
        next = head.next
        head.next = newHead
        return self.doReverse(next, head)


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution2().reverseList(head)
