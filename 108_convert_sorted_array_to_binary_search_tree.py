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
        return self.sortedArrayToBSTRecu(nums, 0, len(nums))
    def sortedArrayToBSTRecu(self, nums, left, right):
        if left >= right:
            return None
        mid = (left + right) / 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBSTRecu(nums, left, mid)
        node.right = self.sortedArrayToBSTRecu(nums, mid + 1, right)
        return node
