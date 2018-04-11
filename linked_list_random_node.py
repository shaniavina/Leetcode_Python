# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from random import randint
class Solution(object):
    def __init__(self, head):
        self.head = head
        
    def getRandom(self):
        res = self.head.val
        cur, n = self.head.next, 1
        while cur:
            res = cur.val if randint(1, n + 1) == 1 else res
            n += 1
            cur = cur.next
        return res
        
