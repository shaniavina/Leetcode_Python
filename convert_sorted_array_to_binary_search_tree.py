# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.sortedArrayToBSTRec(nums, 0, len(nums))
    def sortedArrayToBSTRec(self, nums, start, end):
        if start == end:
            return None
        mid = start + (end - start) / 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBSTRec(nums, start, mid)
        node.right = self.sortedArrayToBSTRec(nums, mid + 1, end)
        return node
