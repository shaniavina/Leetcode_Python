# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from random import randint
class Solution(object):
    
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.__head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        res = self.__head.val
        curr, n = self.__head.next, 1
        while curr:
            res = curr.val if randint(1, n + 1) == 1 else res
            curr = curr.next
            n += 1
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
