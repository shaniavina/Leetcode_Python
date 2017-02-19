# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
????????????
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(float("-inf"))
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next

# Time:  O(n)
# Space: O(n)
# Recursive solution.  


##？？？？？？？？？？？？？？？？？？？
class Solution2:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        [begin, end] = self.reverseListRecu(head)
        return begin
    
    def reverseListRecu(self, head):
        if not head:
            return [None, None]
            
        [begin, end] = self.reverseListRecu(head.next)
        
        if end:
            end.next = head
            head.next = None
            return [begin, head]
        else:
            return [head, head]
########??????????????

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
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